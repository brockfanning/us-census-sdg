import censusdata
import yaml
import os
import sys
import importlib
import pandas as pd

# Use these defaults for all indicators.
defaults = {
  'survey': 'acs5',
  'years': [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
  'calculated_values': {},
  'disaggregations': {},
}

# Abort if config file is not present.
if not os.path.isfile('config.yml'):
  print('First make a copy of config.yml.dist, named config.yml, and edit it as needed.')
  sys.exit()

# Load the config settings.
with open('config.yml', 'r') as stream:
  try:
    config = yaml.load(stream)
  except yaml.YAMLError as exc:
    print(exc)

# Construct the geography for the API call.
geography_parts = []
for geo_id in config['geography']:
  geography_parts.append((geo_id, config['geography'][geo_id]))
geo = censusdata.censusgeo(geography_parts)

# Helper function for chunking a list into a list of smaller lists.
def chunk_list(initial_list, chunk_size):
  final_list = []
  for i in range(0, len(initial_list), chunk_size):
    final_list.append(initial_list[i:i+chunk_size])
  return final_list

# Create a folder to output the CSV files.
if not os.path.exists('data'):
  os.mkdir('data')

# Loop through the indicators to generate CSV files.
for file in os.listdir('indicators'):
  basename = os.path.splitext(file)[0]
  indicator_file = importlib.import_module('indicators.' + basename)
  # For each indicator, inherit from the 'defaults' dict.
  indicator = defaults.copy()
  indicator.update(indicator_file.config)
  df = None
  # We'll make separate API calls for each year.
  for year in indicator['years']:
    # Check the variables we're going to need. There is a max of 50 per request.
    variables = list(indicator['variables'].values())
    data = None
    for chunk in chunk_list(variables, 40):
      # Query the Census API.
      data_chunk = censusdata.download(indicator['survey'], year, geo, chunk, key=config['api_key'])
      if data is None:
        data = data_chunk
      else:
        data = pd.concat([data, data_chunk], axis=1)
    # Set the year.
    data['Year'] = year
    # Rename the variable columns so that the lambda functions will work.
    column_map = {indicator['variables'][k] : k for k in indicator['variables']}
    data = data.rename(column_map, axis='columns')
    # Create columns for the calculated values.
    for column in indicator['calculated_values']:
      data[column] = data.apply(indicator['calculated_values'][column], axis=1)
    # Save a copy for the disaggregation rows later.
    disaggregation_base = data.copy()
    # Calculate the headline value.
    data['Value'] = data.apply(indicator['headline'], axis=1)
    # Save the row.
    if df is None:
      df = data
    else:
      df = df.append(data, sort=False)
    # Add additional rows for each disaggregation.
    for key in indicator['disaggregations']:
      row = disaggregation_base.copy()
      # The disaggregation keys are delimited by the | character.
      for category in key.split('|'):
        # Each category is a column/value separated by the : character.
        parts = category.split(':')
        row[parts[0]] = parts[1]
      row['Value'] = row.apply(indicator['disaggregations'][key], axis=1)
      df = df.append(row, sort=False)

  # Drop the variable and calculated columns since we don't need to export them.
  df = df.drop(indicator['variables'].keys(), axis='columns')
  df = df.drop(indicator['calculated_values'].keys(), axis='columns')
  # Round potentially long floats.
  df = df.round(2)
  # Make sure "Year" is first and "Value" is last.
  cols = df.columns.tolist()
  cols.remove('Year')
  cols.insert(0, 'Year')
  cols.remove('Value')
  cols.append('Value')
  df = df[cols]

  # Export the CSV file.
  filename = 'data/indicator_' + basename + '.csv'
  df.to_csv(filename, index=False)
  print('Successfully generated: ' + filename)
import censusdata
import yaml
import os.path
import sys

# TODO: Convert all of this to OO, with each indicator in a separate file.

"""
class CensusStatistic:

  def __init__(self, variables, alias, year, geo, survey):
    self.variables = variables
    self.alias = alias
    self.year = year
    self.survey = survey
    # Perform the API call immediately.


  # Returns a Pandas dataframe containing "Year", "Value"
  def Value(self):


  def
class IndicatorRow:

  def __init__(self, )
class Indicator:

  def __init__(self, variables, calculation, disaggregations, )
"""

# Use these defaults for all indicators.
defaults = {
  'survey': 'acs5',
  'years': [2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017],
  'calculated_values': {},
  'disaggregations': {},
}

# The list of indicators to generate and calculations to perform.
indicators = {
  '5-1-1': {
    # First get all these variables from the Census data.
    'variables': {
      # priv = private school
      # publ = public school
      # none = not enrolled
      # age1 = 3-4 years
      # age2 = 5-9 years
      # age3 = 10-14 years
      # age4 = 15-17 years
      # age5 = 18-19 years
      # age6 = 20-24 years
      # age7 = 25-34 years
      # age8 = 35+ years
      # f = female
      # m = male
      #'all': 'B14003_001E',
      'priv_f': 'B14003_040E',
      'priv_f_age1': 'B14003_041E',
      'priv_f_age2': 'B14003_042E',
      'priv_f_age3': 'B14003_043E',
      'priv_f_age4': 'B14003_044E',
      'priv_f_age5': 'B14003_045E',
      'priv_f_age6': 'B14003_046E',
      'priv_f_age7': 'B14003_047E',
      'priv_f_age8': 'B14003_048E',
      'priv_m': 'B14003_012E',
      'priv_m_age1': 'B14003_013E',
      'priv_m_age2': 'B14003_014E',
      'priv_m_age3': 'B14003_015E',
      'priv_m_age4': 'B14003_016E',
      'priv_m_age5': 'B14003_017E',
      'priv_m_age6': 'B14003_018E',
      'priv_m_age7': 'B14003_019E',
      'priv_m_age8': 'B14003_020E',
      'publ_f': 'B14003_031E',
      'publ_f_age1': 'B14003_032E',
      'publ_f_age2': 'B14003_033E',
      'publ_f_age3': 'B14003_034E',
      'publ_f_age4': 'B14003_035E',
      'publ_f_age5': 'B14003_036E',
      'publ_f_age6': 'B14003_037E',
      'publ_f_age7': 'B14003_038E',
      'publ_f_age8': 'B14003_039E',
      'publ_m': 'B14003_003E',
      'publ_m_age1': 'B14003_004E',
      'publ_m_age2': 'B14003_005E',
      'publ_m_age3': 'B14003_006E',
      'publ_m_age4': 'B14003_007E',
      'publ_m_age5': 'B14003_008E',
      'publ_m_age6': 'B14003_009E',
      'publ_m_age7': 'B14003_010E',
      'publ_m_age8': 'B14003_011E',
      'none_f': 'B14003_049E',
      'none_f_age1': 'B14003_050E',
      'none_f_age2': 'B14003_051E',
      'none_f_age3': 'B14003_052E',
      'none_f_age4': 'B14003_053E',
      'none_f_age5': 'B14003_054E',
      'none_f_age6': 'B14003_055E',
      'none_f_age7': 'B14003_056E',
      'none_f_age8': 'B14003_057E',
      'none_m': 'B14003_021E',
      'none_m_age1': 'B14003_021E',
      'none_m_age2': 'B14003_022E',
      'none_m_age3': 'B14003_023E',
      'none_m_age4': 'B14003_024E',
      'none_m_age5': 'B14003_025E',
      'none_m_age6': 'B14003_026E',
      'none_m_age7': 'B14003_027E',
      'none_m_age8': 'B14003_028E',
    },
    # Next calculate all the values we'll need for this indicator.
    'calculated_values': {
      # stu = enrolled in either public or private school
      'stu_f_age1': lambda x : x['priv_f_age1'] + x['publ_f_age1'],
      'stu_f_age2': lambda x : x['priv_f_age2'] + x['publ_f_age2'],
      'stu_f_age3': lambda x : x['priv_f_age3'] + x['publ_f_age3'],
      'stu_f_age4': lambda x : x['priv_f_age4'] + x['publ_f_age4'],
      'stu_f_age5': lambda x : x['priv_f_age5'] + x['publ_f_age5'],
      'stu_f_age6': lambda x : x['priv_f_age6'] + x['publ_f_age6'],
      'stu_f_age7': lambda x : x['priv_f_age7'] + x['publ_f_age7'],
      'stu_f_age8': lambda x : x['priv_f_age8'] + x['publ_f_age8'],
      'stu_m_age1': lambda x : x['priv_m_age1'] + x['publ_m_age1'],
      'stu_m_age2': lambda x : x['priv_m_age2'] + x['publ_m_age2'],
      'stu_m_age3': lambda x : x['priv_m_age3'] + x['publ_m_age3'],
      'stu_m_age4': lambda x : x['priv_m_age4'] + x['publ_m_age4'],
      'stu_m_age5': lambda x : x['priv_m_age5'] + x['publ_m_age5'],
      'stu_m_age6': lambda x : x['priv_m_age6'] + x['publ_m_age6'],
      'stu_m_age7': lambda x : x['priv_m_age7'] + x['publ_m_age7'],
      'stu_m_age8': lambda x : x['priv_m_age8'] + x['publ_m_age8'],
      'stu_f': lambda x : (x['priv_f'] + x['publ_f']) - (x['stu_f_age1'] + x['stu_f_age8']),
      'stu_m': lambda x : (x['priv_m'] + x['publ_m']) - (x['stu_m_age1'] + x['stu_m_age8']),
      'none_f': lambda x : x['none_f'] - (x['none_f_age1'] + x['none_f_age8']),
      'none_m': lambda x : x['none_m'] - (x['none_m_age1'] + x['none_m_age8']),
      'all_f': lambda x : x['stu_f'] + x['none_f'],
      'all_m': lambda x : x['stu_m'] + x['none_m'],
      'all': lambda x : x['all_f'] + x['all_m'],
    },
    # The headline represents all students (male + female + public + private)
    'headline': lambda x : (x['stu_f'] + x['stu_m']) / x['all'] * 100,
    # Disaggregate by Sex, Age, and Sex/Age combinations.
    'disaggregations': {
      'Sex:Female': lambda x : x['stu_f'] / x['all'] * 100,
      'Sex:Male': lambda x : x['stu_m'] / x['all'] * 100,
      'Age:5 to 9 years': lambda x : (x['stu_m_age2'] + x['stu_f_age2']) / x['all'] * 100,
      'Age:10 to 14 years': lambda x : (x['stu_m_age3'] + x['stu_f_age3']) / x['all'] * 100,
      'Age:15 to 17 years': lambda x : (x['stu_m_age4'] + x['stu_f_age4']) / x['all'] * 100,
      'Age:18 and 19 years': lambda x : (x['stu_m_age5'] + x['stu_f_age5']) / x['all'] * 100,
      'Age:20 to 24 years': lambda x : (x['stu_m_age6'] + x['stu_f_age6']) / x['all'] * 100,
      'Age:25 to 34 years': lambda x : (x['stu_m_age7'] + x['stu_f_age7']) / x['all'] * 100,
      'Sex:Female|Age:5 to 9 years': lambda x : x['stu_f_age2'] / x['all'] * 100,
      'Sex:Female|Age:10 to 14 years': lambda x : x['stu_f_age3'] / x['all'] * 100,
      'Sex:Female|Age:15 to 17 years': lambda x : x['stu_f_age4'] / x['all'] * 100,
      'Sex:Female|Age:18 and 19 years': lambda x : x['stu_f_age5'] / x['all'] * 100,
      'Sex:Female|Age:20 to 24 years': lambda x : x['stu_f_age6'] / x['all'] * 100,
      'Sex:Female|Age:25 to 34 years': lambda x : x['stu_f_age7'] / x['all'] * 100,
      'Sex:Male|Age:5 to 9 years': lambda x : x['stu_m_age2'] / x['all'] * 100,
      'Sex:Male|Age:10 to 14 years': lambda x : x['stu_m_age3'] / x['all'] * 100,
      'Sex:Male|Age:15 to 17 years': lambda x : x['stu_m_age4'] / x['all'] * 100,
      'Sex:Male|Age:18 and 19 years': lambda x : x['stu_m_age5'] / x['all'] * 100,
      'Sex:Male|Age:20 to 24 years': lambda x : x['stu_m_age6'] / x['all'] * 100,
      'Sex:Male|Age:25 to 34 years': lambda x : x['stu_m_age7'] / x['all'] * 100,
    },
  },
  #'5-5-1': {
  #  'variables': {
  #    'female': 'C24010_041E',
  #    'male': 'C24010_005E',
  #  },
  #  'calculation': lambda x : x['female'] / (x['female'] + x['male']) * 100,
  #}
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

# Loop through the indicators to generate CSV files.
for id in indicators:
  # For each indicator, inherit from the 'defaults' dict.
  indicator = defaults.copy()
  indicator.update(indicators[id])
  df = None
  # We'll make separate API calls for each year.
  for year in indicator['years']:
    # Query the Census API.
    data = censusdata.download(indicator['survey'], year, geo, list(indicator['variables'].values()), key=config['api_key'])
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
    print(data)
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
  filename = 'indicator_' + id + '.csv'
  df.to_csv(filename, index=False)
  print('Successfully generated: ' + filename)
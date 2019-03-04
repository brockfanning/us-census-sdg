# This config gets statistics from the US Census intended to apply to the SDG
# indicator 5.1.1. The metric being used here is the percentage of people
# enrolled in school, disaggregated by sex and age group.
config = {
  # These are the variables that will be queried from the US Census API. The
  # labels (such as "priv_f", "priv_f_age1", etc) can be used later to calculate
  # values from these variables. Here is some explanation of the labels:
  # "priv" = private school
  # "publ" = public school
  # "none" = not enrolled
  # "stu" = private school + public school
  # "all" = private school + public school + not enrolled
  # "f" = female, "m" = male
  # "age1" = 3-4 years
  # "age2" = 5-9 years
  # "age3" = 10-14 years
  # "age4" = 15-17 years
  # "age5" = 18-19 years
  # "age6" = 20-24 years
  # "age7" = 25-34 years
  # "age8" = 35+ years
  'variables': {
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
    'none_m_age1': 'B14003_022E',
    'none_m_age2': 'B14003_023E',
    'none_m_age3': 'B14003_024E',
    'none_m_age4': 'B14003_025E',
    'none_m_age5': 'B14003_026E',
    'none_m_age6': 'B14003_027E',
    'none_m_age7': 'B14003_028E',
    'none_m_age8': 'B14003_029E',
  },
  # This set of calculations makes the code in the "lambda" functions easier
  # to understand.
  'calculated_values': {
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
    'all_f_age1': lambda x : x['stu_f_age1'] + x['none_f_age1'],
    'all_f_age2': lambda x : x['stu_f_age2'] + x['none_f_age2'],
    'all_f_age3': lambda x : x['stu_f_age3'] + x['none_f_age3'],
    'all_f_age4': lambda x : x['stu_f_age4'] + x['none_f_age4'],
    'all_f_age5': lambda x : x['stu_f_age5'] + x['none_f_age5'],
    'all_f_age6': lambda x : x['stu_f_age6'] + x['none_f_age6'],
    'all_f_age7': lambda x : x['stu_f_age7'] + x['none_f_age7'],
    'all_f_age8': lambda x : x['stu_f_age8'] + x['none_f_age8'],
    'all_m_age1': lambda x : x['stu_m_age1'] + x['none_m_age1'],
    'all_m_age2': lambda x : x['stu_m_age2'] + x['none_m_age2'],
    'all_m_age3': lambda x : x['stu_m_age3'] + x['none_m_age3'],
    'all_m_age4': lambda x : x['stu_m_age4'] + x['none_m_age4'],
    'all_m_age5': lambda x : x['stu_m_age5'] + x['none_m_age5'],
    'all_m_age6': lambda x : x['stu_m_age6'] + x['none_m_age6'],
    'all_m_age7': lambda x : x['stu_m_age7'] + x['none_m_age7'],
    'all_m_age8': lambda x : x['stu_m_age8'] + x['none_m_age8'],
    'stu_f': lambda x : (x['priv_f'] + x['publ_f']) - (x['stu_f_age1'] + x['stu_f_age8']),
    'stu_m': lambda x : (x['priv_m'] + x['publ_m']) - (x['stu_m_age1'] + x['stu_m_age8']),
    'all_f': lambda x : x['stu_f'] + (x['none_f'] - (x['none_f_age1'] + x['none_f_age8'])),
    'all_m': lambda x : x['stu_m'] + (x['none_m'] - (x['none_m_age1'] + x['none_m_age8'])),
  },
  # The headline represents all students (male + female + public + private)
  'headline': lambda x : (x['stu_f'] + x['stu_m']) / (x['all_f'] + x['all_m']) * 100,
  # Disaggregate by Sex, Age, and Sex/Age combinations.
  'disaggregations': {
    'Sex:Female': lambda x : x['stu_f'] / x['all_f'] * 100,
    'Sex:Male': lambda x : x['stu_m'] / x['all_m'] * 100,
    'Age:5 to 9 years': lambda x : (x['stu_m_age2'] + x['stu_f_age2']) / (x['all_m_age2'] + x['all_f_age2']) * 100,
    'Age:10 to 14 years': lambda x : (x['stu_m_age3'] + x['stu_f_age3']) / (x['all_m_age3'] + x['all_f_age3']) * 100,
    'Age:15 to 17 years': lambda x : (x['stu_m_age4'] + x['stu_f_age4']) / (x['all_m_age4'] + x['all_f_age4']) * 100,
    'Age:18 and 19 years': lambda x : (x['stu_m_age5'] + x['stu_f_age5']) / (x['all_m_age5'] + x['all_f_age5']) * 100,
    'Age:20 to 24 years': lambda x : (x['stu_m_age6'] + x['stu_f_age6']) / (x['all_m_age6'] + x['all_f_age6']) * 100,
    'Age:25 to 34 years': lambda x : (x['stu_m_age7'] + x['stu_f_age7']) / (x['all_m_age7'] + x['all_f_age7']) * 100,
    'Sex:Female|Age:5 to 9 years': lambda x : x['stu_f_age2'] / x['all_f_age2'] * 100,
    'Sex:Female|Age:10 to 14 years': lambda x : x['stu_f_age3'] / x['all_f_age3'] * 100,
    'Sex:Female|Age:15 to 17 years': lambda x : x['stu_f_age4'] / x['all_f_age4'] * 100,
    'Sex:Female|Age:18 and 19 years': lambda x : x['stu_f_age5'] / x['all_f_age5'] * 100,
    'Sex:Female|Age:20 to 24 years': lambda x : x['stu_f_age6'] / x['all_f_age6'] * 100,
    'Sex:Female|Age:25 to 34 years': lambda x : x['stu_f_age7'] / x['all_f_age7'] * 100,
    'Sex:Male|Age:5 to 9 years': lambda x : x['stu_m_age2'] / x['all_m_age2'] * 100,
    'Sex:Male|Age:10 to 14 years': lambda x : x['stu_m_age3'] / x['all_m_age3'] * 100,
    'Sex:Male|Age:15 to 17 years': lambda x : x['stu_m_age4'] / x['all_m_age4'] * 100,
    'Sex:Male|Age:18 and 19 years': lambda x : x['stu_m_age5'] / x['all_m_age5'] * 100,
    'Sex:Male|Age:20 to 24 years': lambda x : x['stu_m_age6'] / x['all_m_age6'] * 100,
    'Sex:Male|Age:25 to 34 years': lambda x : x['stu_m_age7'] / x['all_m_age7'] * 100,
  },
}
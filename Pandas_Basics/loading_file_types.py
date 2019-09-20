import pandas as pd

'''
IMPORT DIFFERENT DATA TYPES AND READ THE CONTENTS
'''
# Import and read a CSV file
df1 = pd.read_csv('datasets/car_crashes.csv')
# print(df1.head())

df2 = pd.read_csv('datasets/brain_networks.csv')
# print(df2.tail())

# Import and read an Excel file
my_excel = pd.read_excel('datasets/car_crashes.xlsx')
# print(my_excel.head())

# Import and read a JSON file
my_json = pd.read_json('datasets/winemag-data.json')
# print(my_json.head())


'''
SET HEADER ROWS
'''
my_excel2 = pd.read_excel('datasets/car_crashes.xlsx', header=None)
# print(my_excel2)

car_crash_headers = my_excel2.columns = ["TOTAL", "SPEEDING", "ALCOHOL", "NOT DISTRACTED",
                                         "NO PREVIOUS", "INS_PREMIUM", "INS_LOSSES", "ST ABBR"]
# print(my_excel2)
my_excel2.set_index("ST ABBR", inplace=True)
# print(my_excel2)


'''
SET INDEX COLUMN
'''
my_excel3 = pd.read_excel('datasets/car_crashes.xlsx')
my_excel3.columns = car_crash_headers
print(my_excel3)
my_excel3.set_index("ST ABBR", inplace=True)
print(my_excel3)

'''
INDEXING AND SLICING
'''
my_excel4 = pd.read_excel('datasets/car_crashes.xlsx')
my_excel4.columns = car_crash_headers
my_excel4.set_index("ST ABBR", inplace=True)

# Grabs the Index to start at through last named(MA - UT) and grabs columns TOTAL - ALCOHOL
print(my_excel4.loc["MA": "UT", "TOTAL": "ALCOHOL"])
# Lists all of the ALCOHOL related crashes for selected slice used above
print(list(my_excel4.loc[:, "ALCOHOL"]))

# Pulls the data from indexes(MA-NH) and the Column info for those indexes(TOTAL-ALCOHOL)
print(my_excel4.iloc[21:29, 0:3])


import pandas as pd
from geopy.geocoders import ArcGIS

# Import and read a CSV file
my_df = pd.read_csv('datasets/target_locations.csv')
# print(my_df.head())

nomin = ArcGIS()
example_nomin = nomin.geocode('400 Oxford Exchange Blvd, Oxford, AL 36203-3459')
# get_lat = example_nomin.latitude()
# get_long = example_nomin.longitude()
# coordinates = get_lat, get_long

my_df['Address'] = my_df['Address.FormattedAddress'] + ', ' + my_df['Address.City'] + ', ' + \
                   my_df['Address.Subdivision'] + ', ' + my_df['Address.PostalCode'] + ', ' + \
                   my_df['Address.CountryName']

my_df['Coordinates'] = my_df['Address'].apply(nomin.geocode)
print(my_df.Coordinates[0].latitude)

my_df['Latitude'] = my_df['Coordinates'].apply(lambda x: x.latitude if x is not None else None)
my_df['Longitude'] = my_df['Coordinates'].apply(lambda x: x.longitude if x is not None else None)

print(my_df[0])

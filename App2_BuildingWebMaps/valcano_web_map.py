import folium
import pandas as pd

# Add data points using specific longitude and latitude locations
# data = pd.DataFrame({
#     'lon': [45.3288, 45.3311, 59.93, 5.33, 45.52, -1.29, -12.97],
#     'lat': [-121.6625, -121.7311, 30.32, -4.03, -73.57, 36.82, -38.5],
#     'name': ['Mt. Hood Meadow', 'Timberlake Lodge', 'St Petersbourg', 'Abidjan', 'Montreal',
#              'Nairobi', 'Salvador'],
# })

# Read the datafile with all volcano locations in the US
data = pd.read_csv('data_files/Volcanoes-USA.txt')
my_map = folium.Map(location=[45.372, -121.697], zoom_start=5, tiles='Stamen Terrain')


# Create a function for coloring the marker's by a volcanoes elevation
def marker_color(elev):
    """
    Args:
        elev:
    """
    if elev in range(0, 1000):
        color = 'green'
    elif elev in range(1001, 3000):
        color = 'orange'
    else:
        color = 'red'
    return color


# Add markers one by one using the data range defined in your dataset
for lat, lon, name, elevation in zip(data['LAT'], data['LON'], data['NAME'], data['ELEV']):
    folium.Marker(location=[lat, lon], popup=name, icon=folium.Icon(marker_color(elevation))).add_to(my_map)

# Save the folium map to a directory as an html file
my_map.save('data_files/us_map.html')

print('Creating a webmap for Volcanoes in the US...')

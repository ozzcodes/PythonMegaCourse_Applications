import folium
import pandas as pd

# Read the datafile with all volcano locations in the US
data = pd.read_csv('data_files/Volcanoes-USA.txt')
my_map = folium.Map(location=[data['LAT'].mean(), data['LON'].mean()], zoom_start=5, tiles='Stamen Terrain')


# Create a function for coloring the marker's by a volcanoes elevation
def marker_color(elev):
    minimum = int(min(data['ELEV']))
    step_value = int((max(data['ELEV']) - min(data['ELEV'])) / 3)

    if elev in range(minimum, minimum + step_value):
        color = 'green'
    elif elev in range(minimum, minimum + step_value * 2):
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

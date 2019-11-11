import folium
import pandas as pd
import json

# Read the datafile with all volcano locations in the US
data = pd.read_csv('data_files/Volcano_US_Data.csv')
my_map = folium.Map(location=[data['LATITUDE'].mean(), data['LONGITUDE'].mean()], zoom_start=5, tiles='Stamen Terrain')


# Create a function for coloring the marker's by a volcanoes elevation
def marker_color(elev):
    """
    Args:
        elev:
    """
    minimum = int(min(data['ELEV']))
    step_value = int((max(data['ELEV']) - min(data['ELEV'])) / 3)

    if elev in range(minimum, minimum + step_value):
        color = 'green'
    elif elev in range(minimum, minimum + step_value * 2):
        color = 'orange'
    else:
        color = 'red'
    return color


# Add the feature group created above to be able to filter out the icons in the Layer Control
feature_group = folium.FeatureGroup(name='Volcano Locations')
feature_active = folium.FeatureGroup(name='Active Volcanoes')

# Add markers one by one using the data range defined in your dataset
for lat, lon, name, elevation, status in zip(data['LATITUDE'], data['LONGITUDE'], data['VOLCANO_NAME'], data['ELEV'],
                                             data['STATUS']):
    feature_active.add_child(
        folium.RegularPolygonMarker(location=[lat, lon], popup=status, number_of_sides=6, radius=15,
                                    tooltip=status)).add_to(my_map)
    feature_group.add_child(folium.Marker(location=[lat, lon], popup=name,
                                          icon=folium.Icon(marker_color(elevation), icon_color='black'))).add_to(my_map)

geojson_layer = my_map.add_child(
    folium.GeoJson(json.load(open('data_files/world_population.json')),
                   name='World Population',
                   style_function=lambda x: {'fillColor': 'green' if x['properties']['POP2005'] <= 10000000
                   else 'orange' if 10000000 < x['properties']['POP2005'] <= 20000000 else 'red'}))

layer_controller = my_map.add_child(folium.LayerControl(position='topright', collapsed=True))

# Save the folium map to a directory as an html file
my_map.save(outfile='output_files/us_map.html')

print('Creating a webmap for Volcanoes in the US...')

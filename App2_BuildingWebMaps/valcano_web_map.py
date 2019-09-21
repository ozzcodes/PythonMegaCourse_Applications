import folium
import pandas as pd

data = pd.DataFrame({
    'lat': [45.3288, 2, 145, 30.32, -4.03, -73.57, 36.82, -38.5],
    'lon': [-121.6625, 49, -38, 59.93, 5.33, 45.52, -1.29, -12.97],
    'name': ['Mt. Hood Meadow', 'Paris', 'melbourne', 'St Petersbourg', 'Abidjan', 'Montreal', 'Nairobi', 'Salvador']
})
print(data)

# Create an empty Map
my_map = folium.Map(location=[45.372, -121.697], zoom_start=12, tiles='Stamen Terrain')

# Add markers one by one using the data range defined in your dataset
for i in range(0, len(data)):
    folium.Marker([data.iloc[i]['lon'], data.iloc[i]['lat']], popup=data.iloc[i]['name']).add_to(my_map)

# Save the folium map to a directory as an html file
my_map.save('data_files/us_map.html')

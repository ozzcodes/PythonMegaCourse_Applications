from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

# Use the data csv file to create a dataframe
df = pd.read_csv('resources/graph_data.csv')
x = df['x']
y = df['y']

# Create output file
output_file('resources/pandas_line_output.html')

f = figure()
f.line(x, y)

show(f)

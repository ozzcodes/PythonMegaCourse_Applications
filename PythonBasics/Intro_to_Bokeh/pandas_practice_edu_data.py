from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas as pd

# Use the data csv file to create a dataframe
df = pd.read_csv('resources/bachelors.csv')
x = df['Year']
y = df['Engineering']

# Create output file
output_file('resources/education_output.html')

f = figure()
f.line(x, y)

show(f)

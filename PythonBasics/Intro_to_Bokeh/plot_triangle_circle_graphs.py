"""
PRACTICE PROBLEM
"""
from bokeh.plotting import figure
from bokeh.io import output_file, show

# Create parameter data
x = [3, 7.5, 10]
y = [3, 6, 9]

# Prepare the output file
output_file('resources/triangle_graph.html')

# Create a figure object
tri_plot = figure()

tri_plot.triangle(x, y)
show(tri_plot)


'''
Create a Circle Graph
'''
# Prepare the output file
output_file('resources/circle_graph.html')

# Create a figure object
cir_plot = figure()

cir_plot.circle(x, y)
show(cir_plot)

import pandas as pd
from bokeh.plotting import figure, output_file, show

data = pd.read_excel('resources/verlegenhuken.xlsx')

p = figure(plot_width=750, plot_height=600, tools='pan')
p.title.text = "Temperature Air Pressure"
p.title.text_color = "Gray"
p.title.text_font = "times"
p.title.text_font_style = "bold"
p.xaxis.minor_tick_line_color = None
p.yaxis.minor_tick_line_color = None
p.xaxis.axis_label = "Temperature (C)"
p.yaxis.axis_label = "Pressure (hPa)"

# Divide by 10 as to not overwhelm the graph and dot size reduced
p.scatter(data['Temperature']/10, data['Pressure']/10, size=0.5)

output_file("resources/weather_data.html")

show(p)

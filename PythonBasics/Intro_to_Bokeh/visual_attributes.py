from bokeh.plotting import figure, output_file, show

# Create the plot figure
p = figure(plot_width=750, plot_height=600, tools='pan, reset')

# Add any attributes to the plot area with styling
p.title.text = "Earthquakes"
p.title.text_color = "#29dd00"
p.title.text_font = "times"
p.title.text_font_size = "24pt"
p.title.text_font_style = "italic"
p.yaxis.minor_tick_line_color = "Yellow"
p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"
p.border_fill_color = '#c3c3c3'

# Create the plot points or lines with any additional attributes
p.line([1, 2, 3, 4, 5], [5, 6, 5, 5, 3], line_width=2, color="red", alpha=0.5)
p.circle([1, 2, 3, 4, 5], [5, 6, 5, 5, 3], size=[i * 2 for i in [8, 12, 14, 15, 20]], color="purple", alpha=0.5)

# Create random rectangle bars with quadrant style plots
p.quad(top=[2, 3, 4], bottom=[1, 2, 3], left=[1, 2, 3],
       right=[1.2, 2.5, 3.7], color="#B3DE69")

show(p)

# Save the file
output_file("resources/visual_scatterplot2.html")

# Show the file on browser
show(p)

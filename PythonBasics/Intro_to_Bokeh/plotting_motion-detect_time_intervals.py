from App6_Webcam_MotionDetector.detect_object import df
from bokeh.plotting import figure, output_file, show

my_plot = figure(x_axis_type='datetime', height=250, width=500, title='Motion Graph - Timestamps')

# Create a plot quadrant for plotting detail
q = my_plot.quad(left=df['Start'], right=df['End'], bottom=0, top=1, color='purple')
output_file('resources/plot_motion-timestamps.html')
show(my_plot)

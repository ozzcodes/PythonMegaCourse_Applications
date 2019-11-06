from App6_Webcam_MotionDetector.detect_object import df
from bokeh.plotting import figure, output_file, show

my_plot = figure(x_axis_type='datetime', height=250, width=500, title='Motion Graph - Timestamps')
my_plot.yaxis.minor_tick_line_color = None
my_plot.ygrid[0].ticker.desired_num_ticks = 1

# Create a plot quadrant for plotting detail
q = my_plot.quad(left=df['Start'], right=df['End'], bottom=0, top=1, color='purple')
output_file('resources/plot_motion-timestamps2.html')

show(my_plot)

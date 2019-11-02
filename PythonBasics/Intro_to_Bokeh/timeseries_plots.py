from bokeh.plotting import figure, output_file, show
import pandas as pd

# df = pd.read_csv(
#     "http://www.google.com/finance/historical?q=NASDAQ:ADBE&startdate=Jan+01%2C+2009&enddate=Aug+2%2C+2012&output=csv",
#     parse_dates=['Date'])

df = pd.read_csv('resources/adbe.csv', parse_dates=['Date'])

my_plot = figure(width=750, height=500, x_axis_type='datetime')

my_plot.line(df['Date'], df['Close'], color='Blue', alpha=0.5)
output_file('resources/time-series_plot.html')
show(my_plot)

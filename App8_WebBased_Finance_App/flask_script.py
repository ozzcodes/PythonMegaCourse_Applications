from flask import Flask, render_template
from pandas.io.msgpack import dump

my_app = Flask(__name__)


# Create an app route for the plot webpage
@my_app.route('/plot/')
def plot():
    from pandas_datareader import data
    from bokeh.plotting import figure, show, output_file
    import datetime
    from bokeh.embed import components
    from bokeh.resources import CDN
    import yfinance as yf

    yf.pdr_override()

    # Create a start and end datetime
    start = datetime.datetime(2019, 5, 1)
    end = datetime.datetime(2019, 10, 31)

    # Read data from a finance site along with the company ticker
    # DataReader places data into a dataframe automatically
    my_data = data.get_data_yahoo(tickers='TSLA', start=start, end=end)

    # Create new column to dataframe, status
    def margin_change(cl, op):
        if cl > op:
            value = 'Increase'
        elif cl < op:
            value = 'Decrease'
        else:
            value = 'Equal'
        return value

    # Create a status column using the margin change function
    my_data['Status'] = [margin_change(cl, op) for cl, op in zip(my_data.Close, my_data.Open)]
    # Create a mid point location
    my_data['Middle'] = (my_data.Open + my_data.Close) / 2
    # Create the maximum height
    my_data['Height'] = abs(my_data.Close - my_data.Open)

    # Update the CSV file data
    # my_data.to_csv('stock_data/tsla_data.csv')
    print(my_data.head())

    # Create variable to represent the plot to be used for the stocks
    plot_data = figure(x_axis_type='datetime', width=1000, height=400, title='Candlestick Chart')
    plot_data.grid.grid_line_alpha = 0.3

    # Create time-chart to show as value intervals
    hours = 24 * 60 * 60 * 1000
    # Create vertical lines in rectangle shape
    plot_data.segment(my_data.index, my_data.High, my_data.index, my_data.Low, color='black')
    # Plot the rectangles with stock data
    plot_data.rect(my_data.index[my_data.Status == 'Increase'], my_data.Middle[my_data.Status == 'Increase'], hours,
                   my_data.Height[my_data.Status == 'Increase'],
                   fill_color='green', line_color='black')
    plot_data.rect(my_data.index[my_data.Status == 'Decrease'], my_data.Middle[my_data.Status == 'Decrease'], hours,
                   my_data.Height[my_data.Status == 'Decrease'],
                   fill_color='red', line_color='black')

    # This prints the plot data components as a tuple
    flask_script, div1 = components(plot_data)
    cdn_js = CDN.js_files[0]
    cdn_css = CDN.css_files

    return render_template('plot.html',
                           flask_script=flask_script,
                           div1=div1,
                           cdn_css=cdn_css,
                           cdn_js=cdn_js)


# Create a root page for homepage
@my_app.route('/')
def home():
    return render_template('home.html')


# Example root to an about page (although not currently linked)
@my_app.route('/about/')
def about():
    return render_template('about.html')


# Run main file (my_app) as a development package
if __name__ == "__main__":
    my_app.run(debug=True)

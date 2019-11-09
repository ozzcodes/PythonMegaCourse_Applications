from pandas_datareader import data
import bokeh
import datetime

# Create a start and end datetime
start = datetime.datetime(2018, 11, 1)
end = datetime.datetime(2019, 11, 1)

# Read data from a finance site along with the company ticker
# DataReader places data into a dataframe automatically
my_data = data.DataReader(name='TSLA', data_source='yahoo', start=start, end=end)
my_data.to_csv('stock_data/tsla_data.csv')
print(my_data.head())

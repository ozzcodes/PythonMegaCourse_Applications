username = 'ozzycodes'

print(username)
print(len(username))

# Continuous loop
'''
while True:
    with open('data_files/random.txt') as file:
        print(file.read())
'''

# Will print out the file contents determined by the
# sleep count in seconds and prints error message if needed
'''
import time
import os

while True:
    if os.path.exists('data_files/random.txt'):
        with open('data_files/random.txt') as file:
            print(file.read())
    else:
        print('File does not exist!')
    time.sleep(10)
'''
# Using 3rd party packages/ modules
import pandas as pd
import time
import os

while True:
    if os.path.exists('data_files/temps_today.csv'):
        my_data = pd.read_csv('data_files/temps_today.csv')
        print(my_data.mean())
    else:
        print('File does not exist!')
    time.sleep(10)

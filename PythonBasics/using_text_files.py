# Read a basic text file from system
data = open('data_files/process_text.txt')
print(data.read())
print(data.read())  # This will return and empty string
content = data.read()

data.close()

# Will print file contents multiple times
with open('data_files/process_text.txt') as my_file:
    content2 = my_file.read()

print(content2)

# Write out to a text file
with open('data_files/random.txt', 'w') as random_file:
    random_file.write('Where is the heavy-hearted kraken?\nThe cannibal burns with desolation, desire the brig.\nYuck,'
                      'ye rough lad- set sails for beauty!')

# Using 'x' will not allow to overwrite a file like 'w'
# Using 'a' will append text to a file (need to add a break-line to format)
# Write out to a text file
with open('data_files/random.txt', 'a+') as append_data:
    append_data.write('\nHello, there!')
    append_data.seek(0)  # Outputs the data specified by location
    content3 = append_data.read()

print(content3)

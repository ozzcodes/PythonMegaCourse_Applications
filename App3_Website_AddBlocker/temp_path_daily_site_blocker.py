import time
from datetime import datetime as dt

host_path = r"C:\Windows\System32\drivers\etc\hosts"
temp_path = 'source_file/hosts'
redirect = '127.0.0.1'
block_list = ['www.facebook.com', 'facebook.com', 'www.twitter.com', 'www.instagram.com']
final_list = [redirect + " " + i for i in block_list]
final_string_block = '\n'.join(final_list)

while True:
    if dt(dt.now().year, dt.now().month, dt.now().day, 8) < dt.now() < dt(dt.now().year, dt.now().month,
                                                                          dt.now().day, 17):
        print('Within time...')
        with open(temp_path, 'r+') as file:
            content = file.read()
            for website in block_list:
                if website in content:
                    pass
                else:
                    file.write(redirect + " " + website + "\n")
    else:
        with open(temp_path, "r+") as file:
            content = file.readlines()
            file.seek(0)
            for line in content:
                if not any(website in line for website in block_list):
                    file.write(line)
            file.truncate()
        print('Fun hours!!')
    time.sleep(5)

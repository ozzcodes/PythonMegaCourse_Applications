import requests
from bs4 import BeautifulSoup

req = requests.get('http://pythonhow.com/example.html')
cont = req.content
print(type(cont))
# print(cont)

# Put the website source code into a beautifulsoup variable and prettify for ease of reading
bsoup = BeautifulSoup(cont, 'html.parser')
# print(bsoup.prettify())

# Pass a dictionary to a class for obtaining website information
web_data = bsoup.find_all("div", {
    "class": "cities",
})

print(web_data)

# Print out the items in all data by header type
for item in web_data:
    print(item.find_all("p")[0].text)


import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

req = urllib.request.urlopen('http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
cont = req.read()

bsoup = BeautifulSoup(cont, "html.parser")
web_data = bsoup.find_all("div", {
    "class": "propertyRow"
})

# Test print of property price tag
web_data[0].find("h4", {
    "class": "propPrice"
}).text.replace("\n", "").replace(" ", "")

# Obtain the page numbers
page_num = bsoup.find_all('a', {
    'class': 'Page'
})[-1].text
print('Number of pages found: ', page_num)

# Create an empty list to store information
my_list = []

# To read multiple webpages (in this case, page 2) - Cached data for century21
base_url = 'http://www.pyclass.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s='

# Grab pages 0 - 30 and iterate pages by 10
for page in range(0, int(page_num) * 10, 10):
    # Print the page links
    print(base_url + str(
        page) + '.html')
    print()
    # Return and connect the page link data
    req = urllib.request.urlopen(base_url + str(
        page) + '.html')
    cont = req.read()
    bsoup = BeautifulSoup(cont, "html.parser")

    web_data = bsoup.find_all("div", {
        "class": "propertyRow"
    })

    # A loop for pulling 8 different fields from a webpage
    for item in web_data:
        # Replace print statements with a dictionary variable
        # noinspection PyDictCreation
        d = {}
        d["Price"] = item.find("h4", {
            "class", "propPrice"
        }).text.replace("\n", "").replace(" ", "")
        d["Address"] = item.find_all("span", {
            "class", "propAddressCollapse"
        })[0].text
        try:
            d["Locality"] = item.find_all("span", {
                "class", "propAddressCollapse"
            })[1].text
        except:
            d['Locality'] = None
        try:
            d["Beds"] = item.find("span", {
                "class", "infoBed"
            }).find("b").text
        except:
            d["Beds"] = None
        try:
            d["Area"] = item.find("span", {
                "class", "infoSqFt"
            }).find("b").text
        except:
            d["Area"] = None
        try:
            d["Full-baths"] = item.find("span", {
                "class", "infoValueFullBath"
            }).find("b").text
        except:
            d["Full-baths"] = None
        try:
            d["Half-baths"] = item.find("span", {
                "class", "infoValueHalfBath"
            }).find("b").text
        except:
            d["Half-baths"] = None

        for column_group in item.find_all("div", {
            "class": "columnGroup"
        }):
            # print(column_group)
            for feature_group, feature_name in zip(column_group.find_all("span", {
                "class": "featureGroup"
            }), column_group.find_all("span", {
                "class": "featureName"
            })):
                if "Lot Size" in feature_group.text:
                    d["Lot Size"] = feature_name.text
        my_list.append(d)

# Place dictionary into pandas dataframe
df = pd.DataFrame(my_list)
print(df)

# Print dataframe to CSV file
df.to_csv('saved_data/real-estate_output.csv')

import urllib.request
from bs4 import BeautifulSoup

req = urllib.request.urlopen('http://www.pythonhow.com/real-estate/rock-springs-wy/LCWYROCKSPRINGS/')
cont = req.read()

bsoup = BeautifulSoup(cont, "html.parser")
web_data = bsoup.find_all("div", {
    "class": "propertyRow"
})

# # Test print of property price tag
# print(web_data[0].find("h4", {
#     "class": "propPrice"
# }).text.replace("\n", "").replace(" ", ""))

# Replace print statements with a dictionary variable
d = {}

# A loop for pulling 8 different fields from a webpage
for item in web_data:
    d["Area"] = item.find("h4", {
        "class", "propPrice"
    }).text.replace("\n", "").replace(" ", "")
    d["Locality"] = item.find_all("span", {
        "class", "propAddressCollapse"})[0].text
    d["Price"] = item.find_all("span", {
        "class", "propAddressCollapse"
    })[1].text
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
                print(feature_name.text)
    print(" ")

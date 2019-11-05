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

for item in web_data:
    print(item.find("h4", {
        "class", "propPrice"
    }).text.replace("\n", "").replace(" ", ""))
    print(item.find_all("span", {
        "class", "propAddressCollapse"})[0].text)
    print(item.find_all("span", {
        "class", "propAddressCollapse"
    })[1].text)
    try:
        print(item.find("span", {
            "class", "infoBed"
        }).find("b").text)
    except:
        print(None)
    try:
        print(item.find("span", {
            "class", "infoSqFt"
        }).find("b").text)
    except:
        print(None)
    try:
        print(item.find("span", {
            "class", "infoValueFullBath"
        }).find("b").text)
    except:
        print(None)
    try:
        print(item.find("span", {
            "class", "infoValueHalfBath"
        }).find("b").text)
    except:
        print(None)

    print(" ")

from bs4 import BeautifulSoup
import requests
URL = "https://www.trendyol.com"
r = requests.get(URL)

soup = BeautifulSoup(r.content, 'html.parser') # If this line causes an error, run 'pip install html5lib' or install html5lib

for link in soup.body.nav.find_all('a'):
    name = link.get("href")
    newURL = URL+ name
    newRequest = requests.get(newURL)
    newSoup = BeautifulSoup(newRequest.content,'html.parser')  # If this line causes an error, run 'pip install html5lib' or install html5lib
    mydivs = newSoup.find_all("div", {"class": "dscrptn"})
    for div in mydivs:
        text = div.get_text()
        lst = text.split(" ")
        totalnumber = lst[-3]
        print(str(name)+ ","+str(newURL)+" "+","+ str(totalnumber))

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.pythonscraping.com/pages/page3.html")

soup_obj = BeautifulSoup(html,"lxml")

for child in soup_obj.find("table",{"id" : "giftList"}).children:  #scrape_shop child
    print(child)

for sibling in soup_obj.find("table",{"id":"giftList"}).tr.next_siblings:  #scrape_shop for siblings
    print(sibling)

print(soup_obj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())


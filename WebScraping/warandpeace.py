from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import *


html = urlopen("http://pythonscraping.com/pages/warandpeace.html")

soup_obj = BeautifulSoup(html,"lxml")

nameList = soup_obj.findAll(text="the prince")

print(len(nameList))

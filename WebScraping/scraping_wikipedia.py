from bs4 import BeautifulSoup as soup
from urllib.request import urlopen as uReq
import re
import datetime
import random

random.seed(datetime.datetime.now())

def getLink(articleUrl):

    my_url = uReq("http://en.wikipedia.org"+articleUrl)

    soup_obj = soup(my_url,"lxml")

    articles = soup_obj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))

    return articles

links = getLink("/wiki/Python_Programming")

while len(links) > 0:
    newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
    print(newArticle)
    links = getLink(newArticle)











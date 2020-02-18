from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import re
import datetime
import random

# random.seed(datetime.datetime.now())

def getLink(articleUrl):
    my_url = urlopen("https://en.wikipedia.org"+articleUrl)
    soup_obj = soup(my_url,"lxml")
    # articles = soup_obj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
    # articles = soup_obj.find("div",{"id":"bodyContent"}).findAll("a",href = re.compile(".*"))
    links = soup_obj.findAll("a")#,href = re.compile((".*")))
    return links

links = getLink("/wiki/Python_(programming_language)")

# while len(links) > 0:
#     newArticle = links[random.randint(0,len(links)-1)].attrs["href"]
#     print(newArticle)
#     links = getLink(newArticle)

for link in links:
    # print(link) # print a tag
    if "href" in link.attrs:       # print link present in attribute href
        print(link.attrs["href"])





from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"lxml")
        title = bsObj.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")

if title == None:
    print("Title not found !!!")
else:
    print(title)

# my_url = uReq('https://en.wikipedia.org/wiki/Kevin_Bacon')

# my_url = uReq("https://en.wikipedia.org/wiki/Python_(programming_language)")
# soup_obj = soup(my_url,"lxml")

# for link in soup_obj.findAll("a"):
#     if "href" in link.attrs:
#         print(link.attrs["href"])

# urls of article pages id = bodyContent -> div
# urls do not contain colons(:)
#urls begin with /wiki/

# articles = soup_obj.find("div",{"id": "bodyContent"}).findAll("a",href = re.compile("^(/wiki/)((?!:).)*$"))
#
# for link in articles:
#     if "href" in link.attrs:
#         print(link.attrs["href"])




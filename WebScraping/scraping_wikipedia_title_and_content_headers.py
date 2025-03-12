from bs4 import BeautifulSoup
from urllib.request import urlopen

my_url = urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")

soup_obj = BeautifulSoup(my_url,"lxml")

print("\n--------------Tile of the page--------------\n",soup_obj.h1.get_text())

print("\n--------------Header of contents--------------\n")

content_headers = soup_obj.findAll("h2")
for i in content_headers:
    print(i.get_text())

print("\n--------------Header of sub contents--------------\n")

sub_content_headers = soup_obj.findAll("h3")
for i in sub_content_headers:
    print(i.get_text().strip())

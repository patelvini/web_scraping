# Automation script which fetch URL of all images using Beautiful Soup.

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

class ImageUrl:

	def findImageUrl(self):

		my_url = urlopen("https://www.pythonscraping.com/pages/page3.html")

		soup_obj = BeautifulSoup(my_url,"lxml")

		image_list = soup_obj.findAll("img",src = re.compile(".*"))

		return image_list


if __name__ == '__main__':
	
	o1 = ImageUrl()
	result = o1.findImageUrl()

	for i in result:
		if "src" in i.attrs:
			print(i.attrs["src"])

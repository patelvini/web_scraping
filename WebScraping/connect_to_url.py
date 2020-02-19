# Automation script which accepts file name. Extract all URLs from that file and connect to that URLs
# Note: - Use Data.txt file for that task.  I have attached in the mail

import re
import webbrowser

with open("Data.txt") as file:
    for line in file:
        urls = re.findall('https?://(?:[-\\w.]|(?:%[\\da-fA-F]{2}))+', line)
    print(urls)

    for i in urls:
    	webbrowser.open(i)


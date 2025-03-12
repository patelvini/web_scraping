# Automation script which downloads specific file and store into the current directory of application.

import requests


my_url = "https://www.google.com/favicon.ico"

r = requests.get(my_url, allow_redirects = True)

open('favicon.ico','wb').write(r.content)
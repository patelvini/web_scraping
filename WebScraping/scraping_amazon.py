from bs4 import BeautifulSoup
import requests
import smtplib
import time

my_url = 'https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i7/dp/B081JXDZFM/ref=sr_1_2_sspa?keywords=macbook&qid=1582018767&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVkVOM09GUTBJR1ZKJmVuY3J5cHRlZElkPUEwOTc0NjE2MTlXWTMzVk8zVE1VMCZlbmNyeXB0ZWRBZElkPUEwNDgzOTU0MjNMRURZQU5TNVdPRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU='


headers = {"User-Agent" : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36'}

def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('patelvini136@gmail.com','luspglgbqzncupym')

    subject = "Price fell down !!!"

    body = "Check the amazon link https://www.amazon.in/Apple-MacBook-16-inch-Storage-Intel-Core-i7/dp/B081JXDZFM/ref=sr_1_2_sspa?keywords=macbook&qid=1582018767&sr=8-2-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEyVkVOM09GUTBJR1ZKJmVuY3J5cHRlZElkPUEwOTc0NjE2MTlXWTMzVk8zVE1VMCZlbmNyeXB0ZWRBZElkPUEwNDgzOTU0MjNMRURZQU5TNVdPRiZ3aWRnZXROYW1lPXNwX2F0ZiZhY3Rpb249Y2xpY2tSZWRpcmVjdCZkb05vdExvZ0NsaWNrPXRydWU="

    msg = f'Subject: {subject} \n\n{body}'

    server.sendmail(
        'patelvini136@gmail.com',
        'godaseakshay24@gmail.com',
        msg
    )

    print("Email sent successfully !!")
    server.quit()


def check_price():
    page =requests.get(my_url,headers=headers)
    soup_obj = BeautifulSoup(page.content,'html.parser')
    # print(soup_obj.prettify())
    # title = soup_obj.find("span",{"class" : "a-size-large"}).get_text()
    # print(title.strip())
    price = soup_obj.find(id = "priceblock_ourprice").get_text()
    price = list(price[2:])
    for i in price:
        if i == ",":
            price.remove(i)
    price = ''.join(price)

    converted_price = float(price)
    print(converted_price)

    if converted_price > 180000.0:
        send_mail()

while True:
    check_price()
    time.sleep(60 * 60)


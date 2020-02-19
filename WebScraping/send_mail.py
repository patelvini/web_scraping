
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
        'patelvini136@gmail.com',
        msg
    )

    print("Email sent successfully !!")
    server.quit()
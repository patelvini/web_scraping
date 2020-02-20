import schedule
import time

def do_work():
	print("Hello!")



schedule.every(5).seconds.do(do_work)
# schedule.every().hour.do(do_work)
# schedule.every().day.at("10:30").do(do_work)
# schedule.every().wednesday.at("1:00").do(do_work)
# schedule.every(5).to(10).minutes.do(do_work)
# schedule.every().minute.at(":17").do(do_work)



while True:
	schedule.run_pending()
	time.sleep(1)
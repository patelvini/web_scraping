import logging 
import time
from logging.handlers import TimedRotatingFileHandler
import send_mail_with_attachment as sm
import Process_monitor_with_memory_usage as pm


class LogFile:

	def create_log(self,path, content):

		logger = logging.getLogger("Rotating Log")

		logger.setLevel(logging.INFO)

		handler = TimedRotatingFileHandler(path, when = "h", interval = 60, backupCount = 5)

		logger.addHandler(handler)

		for i in range(6):
			logger.info(content)
			time.sleep(75)


if __name__ == '__main__':

	o1 = pm.ProcessMonitor()
	res = o1.findProcessList()
	o2 = LogFile()
	
	log_file = "attachment.log"
	o2.create_log(log_file,res)


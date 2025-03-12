import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import Process_monitor_with_memory_usage as pm
import os

class sendMail:

	def __init__(self,process_list):

		self.process_list = process_list

	def makeFile(self):

		dir_name = "1Rivet"

		self.path = os.path.abspath(dir_name)

		self.file_name = "//attachment.txt"
		f = open(self.path+self.file_name,"w")

		for i in self.process_list:
			f.write(str(i))
			f.write("\n")

		f.close()

	def sendAttachment(self):

		from_addr = "patelvini136@gmail.com"
		to_addr = "godaseakshay24@gmail.com"

		msg = MIMEMultipart()

		msg['From'] = from_addr
		msg['To'] = to_addr

		msg['Subject'] = "Ragards Memory usage of running processes"

		body = "Hello ! I am attaching the log file for all running process with its name, pid and Memory usage. \nPFA,\n"

		msg.attach(MIMEText(body,'plain'))

		f_name = "attachment.txt"
		attachment = open(self.path + self.file_name,"rb")

		p = MIMEBase('application','octet-stream')
		p.set_payload((attachment).read())
		encoders.encode_base64(p)

		p.add_header('Content-Disposition', "attachment; filename = %s" % f_name)

		msg.attach(p)

		s = smtplib.SMTP('smtp.gmail.com', 587)

		s.starttls()

		s.login(from_addr,"luspglgbqzncupym")

		text = msg.as_string()

		s.sendmail(from_addr, to_addr, text)

		s.quit()

		print("Mail sent successfully !!")

if __name__ == '__main__':

	obj = pm.ProcessMonitor()
	res = obj.findProcessList()

	send = sendMail(res)
	send.makeFile()
	send.sendAttachment()


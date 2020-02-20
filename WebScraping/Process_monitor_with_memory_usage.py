# Automation script to find all running processes

import psutil

class ProcessMonitor:

	def findProcessList(self):

		list_of_process_names = []

		for process in psutil.process_iter():

			memory_size = process.memory_info().vms
			process_info = process.as_dict(attrs = ['pid','name'])

			list_of_process_names.append(str(process_info) + "memory size:" + str(memory_size))

		return list_of_process_names

if __name__ == '__main__':
	
	p = ProcessMonitor()

	res = p.findProcessList()
	for i in res:
		print(i)
import os
import hashlib


def deleteFile(path):

	print(f" {path} removed !!")

	os.unlink(path)

def getFileList(dir_name):

	list_of_file = os.listdir(dir_name)

	allFiles = []

	for entry in list_of_file:
		full_path = os.path.join(dir_name, entry)

		if os.path.isdir(full_path):
			allFiles = allFiles + getFileList(full_path)
		else:
			allFiles.append(full_path)
	return allFiles

def duplicateFiles(list_of_file):

	length = len(list_of_file)

	try:

		for i in range(0,length):
			f1 = open(list_of_file[i],"r")
			l1 = []

			for k in f1:
				l1.append(k)

			for j in range(i+1,length):
				f2 = open(list_of_file[j],"r")
				l2 = []

				for k in f2:
					l2.append(k)

				flag = 0

				if len(l1) != len(l2):
					continue
				else:
					for x in range(0,len(l1)):
						if l1[x] != l2[x]:
							flag = 1
							break

					if flag == 1:
						continue
					else:
						f1.close()
						f2.close()
						x = list_of_file[j]
						y = list_of_file[i]
						print(f"{x} is same as {y}")
						deleteFile(x)
						del list_of_file[j]
						length -= 1
						break
				f2.close()
			f1.close()
	except:
		pass

def calculate_checksum(list_of_file):

	for i in list_of_file:
		print(i)
		m = hashlib.md5(open(str(i),"rb").read()).hexdigest() 
		print("Checksum : ",m)
		print("--------------------------------------\n")


if __name__ == '__main__':

	dir_name = input("Enter name of directory : ")

	path = os.path.abspath(dir_name)

	print(path)

	list_of_file = getFileList(path)

	print("\n******************All Files******************\n")

	for i in list_of_file:
		print(i)

	print("\n Total no of files : " ,len(list_of_file))

	print("\n******************Checksum of Files******************\n")

	calculate_checksum(list_of_file)

	print("\n******************Duplicate Files******************\n")

	duplicateFiles(list_of_file)

	list_of_file1 = getFileList(path)

	print("\n******************All Files after removed duplicate files******************\n")

	for i in list_of_file1:
		print(i)

	print("\n Total no of files : " ,len(list_of_file1))


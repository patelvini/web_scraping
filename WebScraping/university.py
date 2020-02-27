import re

string_data = "XYZ:MUMBAI UNIVERSITYCREF:PUNE UNIVERSITYBREF:DADAR UNIVERSITYRREF:KOLHAPUR UNIVERCITY LLCREF:SOLAPUR UNIVERSITY"


tags = ['XYZ', 'REF']
letters = ['C','B','R','']
for each_tag in tags:
	if each_tag != 'REF':
		string_data = string_data.replace(each_tag, "|" + each_tag)
	else:
		for j in letters:
			string_data = string_data.replace(each_tag, "|" + j + each_tag)
			break
	continue
print(string_data)









# regx = "(XYZ|[C|B|R]REF|REF):[a-zA-Z\\s]+?(LLC)?(?=(XYZ|[C|B|R]REF)|REF|$)"

# matches = re.finditer(regx, string)

# tag = re.findall(regx, string)
# print(type(tag))

# for match in matches:
# 	tag_list.append(match.group())

# result= "|" + "|".join(tag)
# print(result)
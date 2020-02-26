import re

string_data = "XYZ:MUMBAI UNIVERSITYCREF:PUNE UNIVERSITYBREF:DADAR UNIVERSITYRREF:KOLHAPUR UNIVERCITY LLCREF:SOLAPUR UNIVERSITY"

regx = "(XYZ|CREF|BREF|RREF|REF):[a-zA-Z\\s]+?(LLC)?(?=(XYZ|CREF|BREF|RREF|REF)|$)"

matches = re.finditer(regx, string_data)


tag_list = []

for match in matches:
	tag_list.append(match.group())

result= "|" + "|".join(tag_list)
print(result)



# regex = r"?:(?<!L)[A-Z]?)REF|^(?!\|)"
# subst = r"||\g<0>"
# result = re.sub(regex, subst, test_string)

# print(result)

#-----------------------------------------------------------

# tags = ['XYZ', 'REF']

# letters = ['C','B','R','']


# for each_tag in tags:
# 	if each_tag != 'REF':
# 		string_data = string_data.replace(each_tag, "|" + each_tag)
# 	else:
# 		for j in letters:
# 			string_data = string_data.replace(each_tag, "|" + j + each_tag)
# 			break
# 		break
# 	continue





# print(string_data)
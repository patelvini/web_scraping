import re

test_string = "XYZ:MUMBAI UNIVERSITYCREF:PUNE UNIVERSITYBREF:DADAR UNIVERSITYRREF:KOLHAPUR UNIVERCITY LLCREF:SOLAPUR UNIVERSITY"

regex = r"?:(?<!L)[A-Z]?)REF|^(?!\|)"
subst = r"||\g<0>"
result = re.sub(regex, subst, test_string)

print(result)


# tags = ['XYZ', 'CREF', 'BREF', 'RREF', 'REF']
#
# string_data = 'XYZ:MUMBAI UNIVERSITYCREF:PUNE UNIVERSITYBREF:DADAR UNIVERSITYRREF:KOLHAPUR UNIVERCITY LLCREF:SOLAPUR UNIVERSITY'
#
# for each_tag in tags:
#     result = string_data.replace(each_tag, "|" + each_tag)
#
# print(result)
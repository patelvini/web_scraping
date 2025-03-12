

string_data = "XYZ:MUMBAI UNIVERSITYCREF:PUNE UNIVERSITYBREF:DADAR UNIVERSITYRREF:KOLHAPUR UNIVERCITY LLCREF:SOLAPUR UNIVERSITYREF:VALSAD"

tags = ['XYZ','CREF','BREF','RREF']

for i in range(0,len(tags)):
	string_data = string_data.replace((tags[i]), "|" + tags[i],1)
	x = string_data.find(tags[i])
string_data = string_data[:x+4] + string_data[x+4:].replace('REF','|REF')

print(string_data)

bitdata = input("Enter the bit string-->")
encoded=""
i=0
count = 0
while i < len(bitdata):
	if bitdata[i]=='1' :
		encoded+=bitdata[i]
		count+=1
	else:
		encoded+=bitdata[i]
		count =0
	if count == 5:
		encoded+='0'
		count=0
	i+=1
encoded = "01111110"+encoded+"01111110"
print("The bit stuffed string is..",encoded)
edata = encoded
edata = edata.removeprefix("01111110")
edata = edata.removesuffix("01111110")
edata = edata.replace("111110","11111")
print("actual data is : ",edata)

name = input("Enter the file name:")
try:	
	fptr = open(name,'r');
	list1 =[]
	for line in fptr:
		list1.append(line.strip("\n"))
	list1.sort(key = len)
	print(list1)
	fptr.close()
except FileNotFoundError:
	print("no such file exists..")
print("bye")
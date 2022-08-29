name = input("Enter the file name:")
fptr = open(name,'r');
list1 =[]
for line in fptr:
	list1.append(line.strip("\n"))
list1.sort()
print(list1)
fptr.close()
filename = input("enter the file name:")
stringname = input("/enter the string:")
with open(filename,'r') as fptr:
	list1 = fptr.readlines()
	new_list=[]
	for line in list1:
		if stringname in line:
			new_list.append(line.strip("\n"))
print(new_list)
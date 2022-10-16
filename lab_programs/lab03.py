import os
file_name = input("Enter the file name with extention :")
try:
	with open(file_name,'r') as fptr:
		lines,words,characters = 0,0,0
		for line in fptr:
			lines+=1
			words+=len(line.split(" "))
			for word in line.strip("\n").split(" "):
				characters+=len(word)
			# characters += len(line.strip("\n"))
		fptr.write("sa")
			
	print("there are",lines,"lines")
	print("there are ",words,"words")
	print("there are ",characters,"characters")
except FileNotFoundError:
	print("no such file exists..")
except IOError:
	print("hi")
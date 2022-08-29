import os
file_name = input("Enter the file name:")
with open(file_name,'r') as fptr:
	lines,words,characters = 0,0,0
	for line in fptr:
		lines+=1
		words+=len(line.split())
		characters += len(line)
print("there are",lines,"lines")
print("there are ",words,"words")
print("there are ",characters,"characters")
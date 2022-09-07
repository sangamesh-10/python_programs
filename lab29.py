import sys
try:
	fp = open(sys.argv[1],'r')
	fp.seek(int(sys.argv[2]))
	print(fp.read())
except FileNotFoundError :
	print("there no file with such name..")

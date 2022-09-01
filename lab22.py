import sys
def display_file(file1):
    try:
        with open(file1,'r') as f:
            print(f.read())
    except FileNotFoundError as e:
        print(e)
def copy_files(file1,file2):
    try:
        with open(file1,'r') as f1,open(file2,'a') as f2:
            f2.write("\n")
            for i in f1:
                f2.write(i)
    except FileNotFoundError as  e:
        print(e)
print("before copying contents of files are---->\n\n")
print(sys.argv[1]+" has:")
display_file(sys.argv[1])
print(sys.argv[2]+" has:")
display_file(sys.argv[2])
copy_files(sys.argv[1],sys.argv[2])
print("After copying:\n")
print(sys.argv[1]+" has:")
display_file(sys.argv[1])
print(sys.argv[2]+" has:")
display_file(sys.argv[2])
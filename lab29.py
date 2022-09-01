import sys
import os
# program should be executed in command prompt or terminal, to give filename as an command line argument..
try:
    with open(sys.argv[1],'r') as f:
        cwd = os.getcwd()
        print("file path: %s" % cwd+"\%s"%sys.argv[1])
        print("file opened..")
        print("file content---->")
        print(f.read())
except:
    print("some error occured..")
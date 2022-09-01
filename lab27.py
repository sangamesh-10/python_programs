d = {}
list = []
filename = input("enter the file name: ")
with open(filename,'r') as f:
    for line in f:
        for word in line.strip("\n").split():
            if word in d:
                d[word]+=1
            else:
                d[word]=1
print(d)
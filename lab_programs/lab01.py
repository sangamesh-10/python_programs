details = []
n = int(input(" enter the no of students: "))
for i in range(n):
    l=[]
    l.append(input("Enter the student name:"))
    l.append(int(input("Enter the student age:")))
    details.append(l)
def giveAge(elem):
    return elem[1]
details.sort(key = giveAge)
print(details)
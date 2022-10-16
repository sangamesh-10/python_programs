t1 = 0
t2 = 1
r = int(input("Enter the value:"))
print(t1,t2,end=" ")
for i in range(2,r):
    t3 = t1+t2
    print(t3,end =" ")
    t1 = t2
    t2 = t3
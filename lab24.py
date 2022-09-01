import math as m
input_val = int(input("Enter the number:"))
def isPrime(n):
    flag = 0
    for i in range(2,int(m.sqrt(n))+1):
        if n%i==0:
            flag=1
    if flag == 1:
        return False
    else:
        return True
for i in range(2,input_val+1):
    if isPrime(i):
        print(i)
    else:
        continue
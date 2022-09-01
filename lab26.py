n = int(input("Enter the input value(ie.no of strings you will enter):"))
arr = []
for i in range(n):
    arr.append(input())
# arr.sort()
for j in range(n-1):
    for i in range(len(arr)-1):
        if (arr[i]>arr[i+1]):
            arr[i],arr[i+1]=arr[i+1],arr[i]
print(arr)
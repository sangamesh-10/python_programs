def insertion(list1):
    n=len(list1)
    for i in range(1,n):
        cur=list1[i]
        j=i-1
        while j >= 0 and cur < list1[j]:
            list1[j+1]=list1[j]
            j=j-1
        list1[j+1]=cur
l=[3,7,1,2,4]
insertion(l)
print(l)
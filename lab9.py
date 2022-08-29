def binarySearch(list,lb,ub,key):
	if(lb<=ub):
		mid = lb+ub//2
		if list[mid]==key:
			return mid
		elif key<list[mid]:
			binarySearch(list,lb,mid-1,key)
		else:
			binarySearch(list,mid+1,ub,key)
	return -1
list=[1,2,3,4,5,6,7,8,9]
key = int(input("Enter the key value to be searched:"))
idx =binarySearch(list,0,len(list)-1,key)
if idx== -1:
	print("value not found")
else:
	print("element found at index ",idx)

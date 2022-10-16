array = [1,2,3,4,5,6,7,8,9]
lb = 0
ub = len(array)-1
key  = int(input("Enter the key value to be searched : "))
found = 0
while(lb<=ub):
	mid = (lb+ub)//2
	if array[mid] == key:
		print("the key value is found at index : ",mid)
		found = 1
		break
	elif key<array[mid]:
		ub = mid-1
	else:
		lb = mid+1
if found == 0:
	print("value not found")

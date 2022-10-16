arr = [2,5,1,7,3,6,4]
n = len(arr)
for i in range(n):
	mini = i
	for j in range(i+1,n):
		if arr[j]<arr[mini]:
			mini=j
	arr[i],arr[mini] = arr[mini],arr[i]
print(arr)


n = int(input("enter the no of frames--->"))
frames=[]
frameslength = []
for i in range(n):
	x=input(f"enter the frame {i+1} : ")
	frames.append(x)
	frameslength.append(len(x)+1)
sdata =""
for i in range(n):
	sdata+= str(frameslength[i]) + frames[i]
print(sdata)
received = sdata
k=0
while(k<len(received)):
	nv=""
	while received[k].isnumeric()==True:
		nv+=received[k]
		k+=1
	k-=1
	print(received[k+1:int(nv)+k])
	k = k + int(nv)	
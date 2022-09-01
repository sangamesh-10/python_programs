m1 = [[1,2,3],
      [4,5,6],
      [7,8,1]]
m2 = [[1,2,1],
      [9,4,4],
      [3,0,1]]
m3 =[]
c = len(m1[0])
r = len(m1)
for i in range(r):
    temp = []
    m3.append(temp)
    temp.clear()
    for j in range(c): 
        res = m1[i][j]+m2[i][j]
        temp.append(res)
    
    print(1)
print(m1)   
print(m3)        

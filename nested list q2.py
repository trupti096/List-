list=[[10,20,30],[40,50,60]]
i=0
while i<len(list):
    j=0
    while j<len(list[i]):
        print(i,j,list[i][j])
        j=j+1
    i=i+1
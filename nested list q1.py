list=[10,20,30,40,[50,60]]
i=0
while i<len(list):
    if type (list[i]) is list:
        if len(list[i])>1:
            j=0
            m=len(list[i])
            while j<m:
                print(i,j,list[i][j])
            j=j+1
    else:
        print(i,list[i])
        i=i+1
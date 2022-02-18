list=[2,3,"4",5.6,6,"6","0",6.7,2,3]
i=0
a=[]
b=[]
c=[]
while i<len(list):
    if type(list[i])==str:
        b.append(list[i])
    elif type(list[i])==float:
        c.append(list[i])
    else:
        a.append(list[i])
    i=i+1
print(a,b,c)
a=[1,2,3,4,5,3,5,4]
i=0
e=[]
x=list(a)
while i<len(a):
    if x[i] not in a[i]:
        if x[i]==a[i]:
            e.append(x[i])
    i=i+1
print(e)
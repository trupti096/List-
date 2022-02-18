a=[1,2,[3,4],[5,6],[7],[8,9]]
i=0
b=[]
while i<len(a):
    if type(a[i])==list:
        b.extend(a[i])
    i=i+1
b.insert(0,1)
b.insert(1,2)
print(b)
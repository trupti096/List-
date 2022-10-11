a=[64,1,2,3,5,4,122,49]
i=0
while i<len(a):
    j=0
    while j<len(a):
        if a[i]<a[j]:
            a[i],a[j]=a[j],a[i]
        j=j+1
    i=i+1
print(a)

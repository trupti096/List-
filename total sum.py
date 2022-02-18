list=[10,11,12,13,14,17,18,19]
i=0
number=30
a=[]
while i<len(list):
    j=0
    b=[]
    while j<len(list):
        if list[i]+list[j]==30:
            b.append(list[i])
            b.append(list[j])
            a.append(b)
        j=j+1
    i=i+1
print(a)
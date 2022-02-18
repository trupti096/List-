num=int(input("enter a no="))
i=1
a=[]
while i<=num:
    j=1
    b=[]
    while j<=10:
        x=i*j
        b.append(x)
        j=j+1
    a.append(i)
    a.append(b)
    i=i+1
print(a)
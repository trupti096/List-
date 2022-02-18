num=int(input("enter a no="))
i=0
a=[]
while i<=num:
    j=0
    b=[]
    while j<=i:
        b.append(j)
        j=j+1
    a.append(b)
    i=i+1
print(a)
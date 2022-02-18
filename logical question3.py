num=int(input("enter a no="))
i=0
a=[]
b=[]
c=[]
sum=0
while i<num:
    num1=int(input("enter a no="))
    a.append(num1)
    num2=int(input("enter a no="))
    b.append(num2)
    i=i+1
j=0
while j<len(a):
    sum=a[j]+b[j]
    c.append(sum)
    j=j+1
print(c)
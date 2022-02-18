list=[23,14,56,12,19,9,15,31,42,43]
i=0
c1=0
c2=0
sum1=0
sum2=0
while i<len(list):
    if list[i]%2==0:
        sum1=sum1+list[i]
        c1=c1+1
    else:
        sum2=sum2+list[i]
        c2=c2+1
    i=i+1
print(sum1,"even")
print(sum2,"odd")
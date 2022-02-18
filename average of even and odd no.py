element=[1,2,3,4,5,6,7,8,9,10]
i=0
count1=0
count2=0
sum1=0
sum2=0
while i<len(element):
    if element[i]%2==0:
        sum1=sum1+element[i]
        count1=count1+1
    else:
        sum2=sum2+element[i]
        count2=count2+1
    i=i+1
print("even",sum1/count1)
print("odd",sum2/count2)
print(sum1)
print(sum2)
print(sum1+sum2)
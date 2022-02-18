marks=[23,45,67,89,90,54,34,21,34,23,19,28,10,45,86,87,9]
i=0
less_than50=0
more_than50=0
sum1=0
sum2=0
while i<len(marks):
    if marks[i]<50:
        less_than50=less_than50 + 1
        sum1=sum1=marks[i]+sum1
    else:
        more_than50=more_than50 + 1
        sum2=marks[i]+sum2
    i=i+1
print("marks more than 50:"+str(more_than50))
print("marks less than 50:"+str(less_than50))
print(sum1)
print(sum2)
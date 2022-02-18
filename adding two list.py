list1=["m","na","i","ke"]
list2=["y","me","s","lly"]
i=0
while i<len(list1):
    print(list1[i]+list2[i])
    i=i+1


#or / another method


list1=["m","na","i","ke"]
list2=["y","me","s","lly"]
i=0
a=[]
while i<len(list1):
    sum=list1[i]+list2[i]
    a.append(sum)
    i=i+1
print(a,end=" ")
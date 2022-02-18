list=[6,1,3,5,6,3,1]
i=0
b=[]
product=1
while i<len(list):
    if list[i] in list:
        if list[i] not in b:
            b.append(list[i])
            product=b[i]*product
    i=i+1
print(b)
print(product)
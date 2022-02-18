binary_number=[1,0,0,1,1,0,1,1]
i=0
sum=0
while i<len(binary_number):
    decimal=binary_number[i]*2**(len(binary_number)-(i+1))
    sum=sum+decimal
    i=i+1
print(sum)
numbers=[50,40,23,70,56,12,5,10,7]
i=0
max1=0
max2=0
max3=0
while i<len(numbers):
    if numbers[i]>max1:
        max3=max2
        max2=max1
        max1=numbers[i]
    elif numbers[i]>max2:
        max3=max2
        max2=numbers[i]
    elif numbers[i]>max3:
        max3=numbers[i]
    i=i+1
print("1st max",max1)
print("2nd max",max2)
print("3rd max",max3)
numbers=[50,40,23,70,56,12,5,10,7]
i=1
while i<len(numbers):
    max_numbers=max(numbers)
    i=i+1
    numbers.sort()
print("second max", numbers[-2])


#or


numbers=[50,40,23,70,56,12,5,10,7]
i=0
max1=0
max2=0
while i<len(numbers):
    if numbers[i]>max1:
        max2=max1
        max1=numbers[i]
    elif numbers[i]>max2:
        max2=numbers[i]
    i=i+1
print("1st max",max1)
print("2nd max",max2)
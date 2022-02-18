list=[23,14,56,12,19,9,15,25,31,42,43]
i=0
while i<len(list):
    if list[i]%2==0:
        print(list[i],"even number")
    elif list[i]%2!=0:
        print(list[i],"odd number")
    i=i+1
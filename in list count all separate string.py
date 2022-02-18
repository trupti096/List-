a=["sukanya","trupti","subhashree"]
i=0
while i<len(a):
    j=0
    count=0
    while j<len(a[i]):
        count=count+1
        j=j+1
    print(a[i],count)
    i=i+1
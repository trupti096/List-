list=['abc','xyz','aba','1221']
i=0
count=0
while i<len(list):
    j=0
    count1=0
    while j<len(list[i]):
        k=-1
        while k>=(-len(list[i])):
            if list[i][j]==list[i][k]:
                count1=count1+1
            if count1==2:
                count=count1
            k=k-1
        j=j+1
    i=i+1
print("count=",count)
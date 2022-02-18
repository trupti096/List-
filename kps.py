kps=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
while i<len(kps):
    if kps[i]>10000000:
        print(kps[i],"crorepati")
    elif kps[i]>100000:
        print(kps[i],"lakhpati")
    else:
        print(kps[i],"dilwale")
    i=i+1



#or


kps=[3000,600000,324990909,90990900,30000,5600000,690909090,31010101,532010,510,4100]
i=0
count1=0
count2=0
count3=0
while i<len(kps):
    if kps[i]>10000000:
        count1=count1+1
    elif kps[i]>100000:
        count2=count2+1
    else:
        count3=count3+1
    i=i+1
print(count1,"crorepati")
print(count2,"lakhpati")
print(count3,"dilwale")


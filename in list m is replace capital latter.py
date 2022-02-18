a="mamata"
b=[]
i=0
while i<len(a):
    if a[i] in "m":
        b.append("M")
    else:
        b.append(a[i])
    i=i+1
print(b)
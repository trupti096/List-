magic_square=[[8,3,4],[1,5,9],[6,7,2]]
i=0
r1=0
r2=0
r3=0
c1=0
c2=0
c3=0
d1=0
d2=0
while i<len(magic_square):
    r1=r1+magic_square [0][i]
    r2=r2+magic_square [1][i]
    r3=r3+magic_square [2][i]
    c1=c1+magic_square [i][0]
    c2=c2+magic_square [i][1]
    c3=c3+magic_square [i][2]
    d1=d1+magic_square [i][i]
    d2=d2+magic_square [i][2-i]
    i=i+1
    if r1==r2==r3==c1==c2==c3==d1==d2:
        print("magic square")
print(sum(magic_square[0]))
print(sum(magic_square[1]))
print(sum(magic_square[2]))
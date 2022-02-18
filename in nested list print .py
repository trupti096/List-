
l=[[[[[1,2,3],[4,5,6]]]]]
p=[]
i=0
while i<len(l):
	j=0
	while j<len(l[i]):
		k=0
		while k<len(l[i][j]):
			m=0
			while m<len(l[i][j][k]):
				n=0
				while n<len(l[i][j][k][m]):
					p.append(l[i][j][k][m][n])
					n=n+1
				m=m+1
			k=k+1
		j=j+1
	i=i+1
print(p)
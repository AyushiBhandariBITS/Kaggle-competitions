def p(j):
 A=[r[:]for r in j];n,m=len(j),len(j[0])
 for i in range(n):
  for k in range(m):
   if j[i][k]:
    v=j[i][k]
    for x,y in[(-1,-1),(-1,1),(1,1),(1,-1)]:
     a,b=i+x,k+y
     while 0<=a<n and 0<=b<m:A[a][b]=v;a+=x;b+=y
 return A
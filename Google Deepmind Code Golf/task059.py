def p(m):
 b=[(i,j)for i in(0,4,8)for j in(0,4,8)]
 c=[(len([m[x][y]for x in range(i,i+3)for y in range(j,j+3)if m[x][y]]),
     next((m[x][y]for x in range(i,i+3)for y in range(j,j+3)if m[x][y]),0),i,j) for i,j in b]
 mx=max(x[0]for x in c)
 for n,v,i,j in c:
  for x in range(i,i+3):
   for y in range(j,j+3):
    m[x][y]=v if n==mx else 0
 return m
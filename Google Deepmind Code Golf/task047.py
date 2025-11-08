def p(m):
 c=[(i,j,m[i][j])for i in range(9)for j in range(9)if m[i][j]in(7,8)]
 for i,j,v in c:
  for k in range(9):
   m[i][k]=v if m[i][k]in(0,v)else 2
   m[k][j]=v if m[k][j]in(0,v)else 2
 return m
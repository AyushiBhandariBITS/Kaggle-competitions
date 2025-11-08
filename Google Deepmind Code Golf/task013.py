def p(m):
 R,C=len(m),len(m[0])
 if C>=R:x=[(i,m[0][i]or m[-1][i])for i in range(C)if m[0][i]or m[-1][i]];L=C;S=R;c=1
 else:   x=[(i,m[i][0]or m[i][-1])for i in range(R)if m[i][0]or m[i][-1]];L=R;S=C;c=0
 d=x[1][0]-x[0][0];a,b=x
 for k in range(a[0],L,d*2):
  if c:
   for r in range(S):m[r][k]=a[1]
   if k+d<L:
    for r in range(S):m[r][k+d]=b[1]
  else:
   m[k]=[a[1]]*S
   if k+d<L:m[k+d]=[b[1]]*S
 return m
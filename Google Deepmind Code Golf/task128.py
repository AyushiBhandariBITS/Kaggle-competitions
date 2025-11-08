def p(m):
 n=len(m);r=[[0]*len(m[0])for _ in m]
 for j in range(len(m[0])):
  c=[m[i][j]for i in range(n)];k=sum(v!=0 for v in c)
  for i,v in enumerate(c):r[i-k][j]=v if v else 0
 return r
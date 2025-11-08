def p(m):
 n,c=len(m),len(m[0]);q={}
 for r in m:
  for x in r:
   if x:q[x]=q.get(x,0)+1
 if not q:return m
 v=min(q,key=lambda k:(q[k],k));o=[[0]*c for _ in range(n)]
 for i in range(n):
  for j in range(c):
   if m[i][j]==v:
    for a in range(i-1,i+2):
     for b in range(j-1,j+2):
      if 0<=a<n and 0<=b<c:o[a][b]=2
    o[i][j]=v;return o
 return m
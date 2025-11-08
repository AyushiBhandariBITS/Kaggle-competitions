def p(j):
 A=[r[:]for r in j];C,R=len(j),len(j[0])
 for i in range(C):
  for k in range(R):
   if j[i][k]==3 and any(0<=i+a<C and 0<=k+b<R and j[i+a][k+b]==3 for a,b in((0,1),(1,0),(0,-1),(-1,0))):A[i][k]=8
 return A
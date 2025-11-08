def p(j):
 c=len(j);E=[[0]*c for _ in[0]*c]
 for k in range(c):
  for w in range(c):
   if j[k][w]==5:
    for l in range(max(0,k-1),min(c,k+2)):
     for J in range(max(0,w-1),min(c,w+2)):E[l][J]=1
 return E
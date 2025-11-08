def p(g,L=len,R=range):
 c=0;C=[]
 for r in g:
  K=[r[0]];[K.append(r[i+1])for i in R(L(r)-1)if r[i+1]!=r[i]]
  if L(K)>c:c=L(K);C=K[:]
 g=[C[:]for _ in R(L(C))]
 for r in R(L(g)//2):
  for c in R(r,L(C)-r-1):g[r][c]=g[r][r];g[-r-1][c]=g[-r-1][r]
 return g
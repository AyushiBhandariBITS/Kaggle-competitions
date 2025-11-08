def p(g,L=len,R=range):
 g=g[0];C=g[0];T=L([x for x in g if x>0]);w=L(g);h=w//2
 X=[[0]*w for _ in R(h)]
 for r in R(h):
  for c in R(w):
   if c<T:X[r][c]=C
  T+=1
 return X
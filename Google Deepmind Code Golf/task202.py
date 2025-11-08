def p(g):
 T=lambda a:[list(r)for r in zip(*a)]
 H=lambda a:any(len(set(r))==1for r in a)
 G=[r[:]for r in g];t=0
 if not H(G):G=T(G);t=1
 h,w=len(G),len(G[0]);P={}
 for i in range(h):
  for j in range(w):
   v=G[i][j]
   if v:P.setdefault(v,[]).append((i,j))
 O=[r[:]for r in G]
 for v,S in P.items():
  i0=min(i for i,_ in S);i1=max(i for i,_ in S)
  j0=min(j for _,j in S);j1=max(j for _,j in S)
  Z={j for j in range(j0,j1+1)if any(G[i][j]==0for i in range(i0,i1+1))}
  for i,j in S:
   if j in Z:O[i][j]=0
 if t:O=T(O)
 return O
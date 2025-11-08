def p(g):
 h,w=len(g),len(g[0])
 d={}
 for r,R in enumerate(g):
  for c,v in enumerate(R):
   if v:d.setdefault(v,[[],[]]);d[v][0]+=[r];d[v][1]+=[c]
 C=min(d,key=lambda k:len(d[k][1])-max(d[k][0])/100)
 g=[[v if v==C else 0 for v in r]for r in g]
 for r in range(h):
  if g[r][0]==C or g[r][-1]==C:g[r]=[C]*w
 for c in range(w):
  if g[0][c]==C or g[-1][c]==C:
   for r in range(h):g[r][c]=C
 return g
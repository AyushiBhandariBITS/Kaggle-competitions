def p(g):
 for r in range(4):
  for c in range(4):
   if g[r][c]==0:
    for a,b in((0,5),(5,0),(5,5)):
     if g[r+a][c+b]>0:g[r][c]=g[r+a][c+b];break
 return[g[i][:4]for i in range(4)]
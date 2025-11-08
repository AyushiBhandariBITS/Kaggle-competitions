def p(g):
 for r in range(len(g)):
  for c in range(len(g[0])):
   for v,d in[(2,[(1,1),(-1,-1),(-1,1),(1,-1)]),(1,[(0,1),(0,-1),(-1,0),(1,0)])]:
    if g[r][c]==v:
     for i,j in d:g[r+i][c+j]=4+(v==1)*3
 return g
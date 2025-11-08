def p(g):
 for r in range(len(g)):
  for c in range(len(g[0])):
   if g[r][c]==2:
    H=g[r+1].count(3)>1
    for y in range(3):
     for x in range(3):
      g[r+y+2*(not H)][c+x+2*H]=g[r+y][c+x]
      if g[r+y][c+x]==2and(x<2 if H else y<2):g[r+y][c+x]=0
    return g
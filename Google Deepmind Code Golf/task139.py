def p(g):
 for i in range(len(g)-2):
  for j in range(len(g[0])-2):
   r=range(i,i+3);c=range(j,j+3)
   if all(4 in x for x in[g[i][j:j+3],g[i+2][j:j+3],[g[y][j]for y in r],[g[y][j+2]for y in r]]):
    for y in r:
     for x in c:g[y][x]+=7*(g[y][x]==0)
 return g
def p(g):
 for x in range(len(g[0])):
  if g[-1][x]==2:
   c=0
   for y in range(len(g)):
    if g[-1-y][x+c]==5:c+=1;g[-y][x+c]=2
    g[-1-y][x+c]=2
 return g
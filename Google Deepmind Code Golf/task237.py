def p(g):
 for r in range(len(g)):
  s=0
  for c in range(len(g[0])):s=g[~r][c]or s;g[~r][c]=s
  s=0
  for r in range(len(g)):s=g[r][-1]or s;g[r][-1]=s
 return g
def p(g,V=range):
 r=[x[:]for x in g];v=set()
 for i in V(len(g)-2):
  for j in V(len(g[0])):
   if g[i][j]and(i,j)not in v:
    c=g[i][j];a=j
    if all(g[i+k][j]==c for k in V(3)):
     while a<len(g[0])and all(g[i+k][a]==c for k in V(3)):
      for k in V(3):v|={(i+k,a)}
      a+=1
     for x in V(j,a):
      if(x-j)%2:r[i+1][x]=0
 return r
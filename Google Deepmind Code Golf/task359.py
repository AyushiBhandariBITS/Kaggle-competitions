def X(g):return list(zip(*g[::-1]))
def p(g):
 v=0
 if max(g[0].count(i)for i in range(10))-1<len(g[0])/2:v=1;g=X(g)
 for r in range(len(g)):
  c=max(range(10),key=g[r].count)
  g[r]=[c]*len(g[0])
 if v:g=X(X(X(g)))
 return [list(r)for r in g]
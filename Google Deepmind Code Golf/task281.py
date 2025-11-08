from collections import Counter as C
def p(g):
 h,w=len(g),len(g[0])
 b=C([v for r in g for v in r]).most_common(1)[0][0]
 i=[(x,y)for x in range(h)for y in range(w)if g[x][y]!=b]
 if not i:return [r[:]for r in g]
 f=lambda G:min(set(v for r in G for v in r),key=lambda x:[v for r in G for v in r].count(x))
 r=lambda G,a,b:[[b if v==a else v for v in row]for row in G]
 G=r(g,8,0);c1=f(G);c2=f(r(G,c1,0))
 u,l=min(x for x,_ in i),max(x for x,_ in i)
 v,w=min(y for _,y in i),max(y for _,y in i)
 o=[row[:]for row in g]
 for x in range(u,l+1):
  for y in range(v,w+1):o[x][y]=c1
 for y in range(v,w+1):o[u][y]=o[l][y]=c2
 for x in range(u,l+1):o[x][v]=o[x][w]=c2
 return o
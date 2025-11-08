from collections import deque
def p(g):
 h,w=len(g),len(g[0]);v={x for r in g for x in r}
 bg=8if 8in v else max(v,key=lambda x:sum(r.count(x)for r in g))
 c=sorted(x for x in v if x not in(0,bg))
 if len(c)!=2:return g
 a,b=c;G=[r[:]for r in g];s=[[0]*w for _ in g];q=deque()
 for i in range(h):
  for j in range(w):
   if G[i][j]in(a,b):q+=[(i,j,G[i][j])];s[i][j]=1
 while q:
  i,j,t=q.popleft()
  for di,dj in((1,0),(-1,0),(0,1),(0,-1)):
   x,y=i+di,j+dj
   if 0<=x<h and 0<=y<w and not s[x][y]:
    if G[x][y]==0:n=b if t==a else a;G[x][y]=n;q+=[(x,y,n)]
    s[x][y]=1
 return G
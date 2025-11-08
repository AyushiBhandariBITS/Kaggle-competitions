from collections import Counter,deque
def p(g):
 h,w=len(g),len(g[0])
 n={(i,j)for i in range(min(3,h))for j in range(min(3,w))if g[i][j]}
 if not n:return [r[:]for r in g]
 mi,mj=min(i for i,_ in n),min(j for _,j in n)
 p={(i-mi,j-mj)for i,j in n}
 b=Counter(v for r in g for v in r).most_common(1)[0][0]
 o=[r[:]for r in g]
 s=[[0]*w for _ in range(h)]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=b and not s[i][j]:
    c=g[i][j];q=deque([(i,j)]);s[i][j]=1;v=[]
    while q:
     x,y=q.popleft();v+=[(x,y)]
     for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
      u,vv=x+dx,y+dy
      if 0<=u<h and 0<=vv<w and not s[u][vv] and g[u][vv]==c:s[u][vv]=1;q.append((u,vv))
    if {(x-min(x for x,_ in v),y-min(y for _,y in v))for x,y in v}==p:
     for x,y in v:o[x][y]=5
 for i in range(min(3,h)):
  for j in range(min(3,w)):o[i][j]=g[i][j]
 return o
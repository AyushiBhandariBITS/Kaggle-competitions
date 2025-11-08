from collections import deque as D
def p(g):
 h,w=len(g),len(g[0]);o=[r[:]for r in g];v=[[0]*w for _ in range(h)]
 for i in range(h):
  for j in range(w):
   if g[i][j]==6 and not v[i][j]:
    q=D([(i,j)]);c=[];v[i][j]=1
    while q:
     x,y=q.popleft();c+=[(x,y)]
     for a,b in((1,0),(-1,0),(0,1),(0,-1)):
      u,vv=x+a,y+b
      if 0<=u<h and 0<=vv<w and not v[u][vv] and g[u][vv]==6:v[u][vv]=1;q+=[(u,vv)]
    X=[x for x,_ in c];Y=[y for _,y in c];mi,ma,mj,mb=min(X),max(X),min(Y),max(Y)
    for y in range(mj-1,mb+2):
     if 0<=mi-1<h:o[mi-1][y]=3
     if 0<=ma+1<h:o[ma+1][y]=3
    for x in range(mi-1,ma+2):
     if 0<=mj-1<w:o[x][mj-1]=3
     if 0<=mb+1<w:o[x][mb+1]=3
    s=set(c)
    for x in range(mi,ma+1):
     for y in range(mj,mb+1):
      if(x,y)not in s:o[x][y]=4
 return o
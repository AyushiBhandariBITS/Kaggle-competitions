def p(g):
 from collections import Counter,deque
 h,w=len(g),len(g[0])
 f=lambda s,c=max: c(Counter(v for r in s for v in r),key=lambda x:Counter(v for r in s for v in r)[x])
 def n(i,j):
  for a,b in((1,0),(-1,0),(0,1),(0,-1)):
   x,y=i+a,j+b
   if 0<=x<h and 0<=y<w:yield x,y
 def objs(t):
  bg=f(t)
  s=[[0]*w for _ in range(h)]
  o=[]
  for i in range(h):
   for j in range(w):
    if s[i][j]:continue
    v=t[i][j]
    if v==bg:s[i][j]=1;continue
    q=deque([(i,j)]);s[i][j]=1;c=[]
    while q:
     a,b=q.popleft()
     if t[a][b]!=v:continue
     c.append((a,b))
     for x,y in n(a,b):
      if not s[x][y]:s[x][y]=1;q.append((x,y))
    if c:o.append((v,c))
  return o
 def box(p):
  i,j=zip(*p)
  return min(i),min(j),max(i),max(j)
 d=lambda p:set((x,y)for x in range(box(p)[0],box(p)[2]+1)for y in range(box(p)[1],box(p)[3]+1))-set(p)
 c=lambda i,j,k:sum(g[a][b]==k for a,b in n(i,j))
 def shoot(s,dv):
  di,dj=dv;di=(di>0)-(di<0);dj=(dj>0)-(dj<0)
  a,b=s;r=[]
  for k in range(43):
   x,y=a+di*k,b+dj*k
   if 0<=x<h and 0<=y<w:r.append((x,y))
  return r
 lc=f(g,min)
 sc,dc=set(),set()
 for col,pts in objs(g):
  dd=d(pts)
  if not dd:continue
  st=next(iter(dd))
  ca=None
  for i,j in pts:
   if c(i,j,lc)==2:ca=(i,j);break
  if not ca:ca=min(pts)
  di,dj=st[0]-ca[0],st[1]-ca[1]
  sc|=set(shoot(st,(di,dj)));dc|=dd
 o=[r[:]for r in g]
 for i,j in sc:o[i][j]=lc
 for i,j in dc:o[i][j]=0
 return o
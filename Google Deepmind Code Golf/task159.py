def a(G):
 f=[v for r in G for v in r]
 return max(set(f),key=f.count)
def b(G):
 bg=a(G);h,w=len(G),len(G[0]);s=[[0]*w for _ in range(h)];C=[]
 for i in range(h):
  for j in range(w):
   if s[i][j]or G[i][j]==bg:continue
   c=G[i][j];q=[(i,j)];s[i][j]=1;cur=[]
   while q:
    x,y=q.pop();cur.append((x,y,c))
    for dx in(-1,0,1):
     for dy in(-1,0,1):
      if dx==dy==0:continue
      X,Y=x+dx,y+dy
      if 0<=X<h and 0<=Y<w and not s[X][Y]and G[X][Y]==c:s[X][Y]=1;q.append((X,Y))
   C.append(cur)
 return C
def c(o):
 mi=min(i for i,_,_ in o);mj=min(j for _,j,_ in o)
 return[(i-mi,j-mj,v)for i,j,v in o]
def d(o,k):
 if k==1:return list(o)
 r=[]
 for i,j,v in o:
  for di in range(k):
   for dj in range(k):r.append((i*k+di,j*k+dj,v))
 return r
def e(I):
 h,w=len(I),len(I[0])
 p=[(i,j)for i in range(h)for j in range(w)if I[i][j]==2]
 if not p:return tuple(map(tuple,I))
 i0=min(i for i,_ in p);j0=min(j for _,j in p)
 i1=max(i for i,_ in p);j1=max(j for _,j in p)
 S=[list(I[i][j0:j1+1])for i in range(i0,i1+1)]
 sh,sw=len(S),len(S[0])
 m=b(I)
 if not m:return tuple(map(tuple,S))
 s=min(m,key=len);k=sw//3
 o=c(d(s,k));o=[(i+1,j+1,v)for i,j,v in o]
 for i,j,v in o:
  if 0<=i<sh and 0<=j<sw:S[i][j]=v
 return tuple(map(tuple,S))
def p(g):return [list(r)for r in e(tuple(map(tuple,g)))]
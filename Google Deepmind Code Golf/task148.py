from collections import Counter as C
def p(g):
 h,w=len(g),len(g[0]);G=[r[:]for r in g];bg=max(C(v for r in g for v in r),key=C(v for r in g for v in r).get)
 e=[(i,j) for i in range(h) for j in range(w) if g[i][j]==8]
 for i,j in e:G[i][j]=4
 def u(i,j):
  if 0<=i<h and 0<=j<w and G[i][j]==bg:G[i][j]=8
 for i,j in e:
  l=r=None
  for k in range(j-1,-1,-1):
   if g[i][k]==2:l=k;break
  for k in range(j+1,w):
   if g[i][k]==2:r=k;break
  t=None
  if l!=None and r!=None:t=l if j-l<=r-j else r
  else:t=l if l!=None else r
  if t!=None:
   for x in range(min(j,t),max(j,t)+1):u(i,x)
 s=[[0]*w for _ in range(h)];c=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]==2 and not s[i][j]:
    q=[(i,j)];s[i][j]=1;comp=[]
    while q:
     a,b=q.pop();comp.append((a,b))
     for dx,dy in ((1,0),(-1,0),(0,1),(0,-1)):
      x,y=a+dx,b+dy
      if 0<=x<h and 0<=y<w and not s[x][y] and g[x][y]==2:s[x][y]=1;q.append((x,y))
    c.append(comp)
 di=max(min(i for i,_ in comp) for comp in c)-min(min(i for i,_ in comp) for comp in c) if c else 0
 for i,j in e:
  ni=i+di
  if 0<=ni<h:
   for jj in range(w):u(ni,jj)
 return G
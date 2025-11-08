def p(g):
 h,w=len(g),len(g[0]);f=[v for r in g for v in r];b=max(set(f),key=f.count)
 v=[[0]*w for _ in range(h)];o=[]
 for i in range(h):
  for j in range(w):
   if v[i][j]or g[i][j]==b:v[i][j]=1;continue
   c=g[i][j];s=[(i,j)];v[i][j]=1;cells=[]
   while s:
    x,y=s.pop()
    if g[x][y]!=c:continue
    cells+=[(x,y)]
    for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
     nx,ny=x+dx,y+dy
     if 0<=nx<h and 0<=ny<w and not v[nx][ny]:v[nx][ny]=1;s.append((nx,ny))
   if cells:o.append((c,cells))
 C=[]
 for c,cells in o:
  mi=min(x for x,_ in cells);ma=max(x for x,_ in cells)
  mj=min(y for _,y in cells);mb=max(y for _,y in cells)
  C+=[(mi+(ma-mi+1)//2,mj+(mb-mj+1)//2)]
 R=[r[:] for r in g]
 for i in range(h):
  for j in range(w):
   d=[abs(i-ci)+abs(j-cj) for ci,cj in C]
   m=min(d)
   if d.count(m)!=1:continue
   k=d.index(m);ci,cj=C[k]
   if max(abs(i-ci),abs(j-cj))%2==0:R[i][j]=o[k][0]
 return R
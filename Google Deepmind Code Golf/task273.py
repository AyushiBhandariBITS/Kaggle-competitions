def p(j):
 H,W=len(j),len(j[0]);F=[(y,x)for y in range(H)for x in range(W)if j[y][x]==4];S=set()
 for a in range(len(F)):
  y1,x1=F[a]
  for b in range(a,len(F)):
   y2,x2=F[b]
   if y1==y2:
    for x in range(min(x1,x2),max(x1,x2)+1):S|={(y1,x)}
   if x1==x2:
    for y in range(min(y1,y2),max(y1,y2)+1):S|={(y,x1)}
 f=[v for r in j for v in r];bg=max(set(f),key=f.count);G=[r[:]for r in j]
 for y,x in S:
  if 0<=y<H and 0<=x<W and G[y][x]==bg:G[y][x]=-1
 v=[[0]*W for _ in j];C=[]
 for y in range(H):
  for x in range(W):
   if G[y][x]!=bg and not v[y][x]:
    q=[(y,x)];v[y][x]=1;c=[]
    while q:
     i,k=q.pop();c+=[(i,k)]
     for d,e in((1,0),(-1,0),(0,1),(0,-1)):
      a,b=i+d,k+e
      if 0<=a<H and 0<=b<W and not v[a][b]and G[a][b]!=bg:v[a][b]=1;q+=[(a,b)]
    C+=[c]
 for c in C:
  Y=[i for i,_ in c];X=[k for _,k in c];y0,y1=min(Y)+1,max(Y)-1;x0,x1=min(X)+1,max(X)-1
  for i in range(y0,y1+1):
   for k in range(x0,x1+1):
    if 0<=i<H and 0<=k<W:G[i][k]=2
 for i in range(H):
  for k in range(W):
   if G[i][k]==-1:G[i][k]=0
 return G
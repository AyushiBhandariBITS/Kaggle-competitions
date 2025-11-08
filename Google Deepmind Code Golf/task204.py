def p(g):
 h,w=len(g),len(g[0]);o=[r[:]for r in g];v=[[0]*w for _ in g];d=[(1,0),(-1,0),(0,1),(0,-1)]
 for i in range(h):
  for j in range(w):
   if v[i][j]:continue
   c=g[i][j];q=[(i,j)];v[i][j]=1;s=[(i,j)];mi=ma=i;mj=mx=j
   while q:
    x,y=q.pop()
    for dx,dy in d:
     X,Y=x+dx,y+dy
     if 0<=X<h and 0<=Y<w and not v[X][Y]and g[X][Y]==c:
      v[X][Y]=1;q+=[(X,Y)];s+=[(X,Y)]
      mi=min(mi,X);ma=max(ma,X);mj=min(mj,Y);mx=max(mx,Y)
   H,W=ma-mi+1,mx-mj+1
   if H==W==int(len(s)**.5):n=2if H%2<1 else 7;[o.__setitem__(x,o[x][:y]+[n]+o[x][y+1:])for x,y in s]
 return o
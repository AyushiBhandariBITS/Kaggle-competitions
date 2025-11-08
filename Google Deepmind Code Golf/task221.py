def p(g):
 G=[r[:]for r in g];h,w=len(G),len(G[0])if G else 0;z=sum(v==0 for r in G for v in r)
 for i in G:i+=[0]*max(0,3*z*z-3)
 H,W=h,len(G[0]);f=[v for r in G for v in r]
 if not f:return[g for g in G]
 b=max(set(f),key=f.count);s=[[0]*W for _ in range(H)];c=[]
 for i in range(H):
  for j in range(W):
   if G[i][j]==b or s[i][j]:continue
   v=G[i][j];q=[(i,j)];s[i][j]=1;t=[]
   while q:
    x,y=q.pop();t+=[(x,y,v)]
    for a in(-1,0,1):
     for d in(-1,0,1):
      X,Y=x+a,y+d
      if(a or d)and 0<=X<H and 0<=Y<W and not s[X][Y]and G[X][Y]==v:s[X][Y]=1;q+=[(X,Y)]
   c+=[t]
 for k in range(max(0,9-z)):
  for t in c:
   for x,y,v in t:Y=y+3*k;0<=Y<W and(G[x].__setitem__(Y,v))
 sw=W//z;o=1 if W%z else 0;return[r for i in range(z)for r in[r[sw*i+i*o:sw*(i+1)+i*o]for r in G]]
def p(g):
 h,w=len(g),len(g[0]);v=set();r=[x[:]for x in g];c=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=2 and(i,j)not in v:
    q=[(i,j)];v|={(i,j)};z=[];n=0
    while q:
     x,y=q.pop();z+=[(x,y)];n+=g[x][y]==0
     for a,b in((1,0),(-1,0),(0,1),(0,-1)):
      X,Y=x+a,y+b
      if 0<=X<h and 0<=Y<w and g[X][Y]!=2 and(X,Y)not in v:v|={(X,Y)};q+=[(X,Y)]
    c+=[(n,z)]
 d,m=max(x for x,_ in c),min(x for x,_ in c)
 for n,z in c:
  for x,y in z:
   if g[x][y]==0:r[x][y]=1*(n==d)+8*(n==m)*bool(n!=d)
 return r
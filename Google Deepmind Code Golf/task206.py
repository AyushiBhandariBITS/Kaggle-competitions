from collections import*
def p(g):
 h,w=len(g),len(g[0]);b=Counter(x for r in g for x in r).most_common(1)[0][0];v=[[0]*w for _ in g];C=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]==b or v[i][j]:continue
   q=deque([(i,j)]);v[i][j]=1;c=[]
   while q:
    x,y=q.popleft();c+=[(x,y)]
    for X,Y in((1,0),(-1,0),(0,1),(0,-1)):
     a,bx=x+X,y+Y
     if 0<=a<h and 0<=bx<w and not v[a][bx]and g[a][bx]!=b:v[a][bx]=1;q+=[(a,bx)]
   C+=[c]
 G,O=[c for c in C if any(g[i][j]==5 for i,j in c)],[c for c in C if all(g[i][j]!=5 for i,j in c)];G,O=G[0],O[0]
 gi,gj=zip(*G);ci,cj=(min(gi)+max(gi))//2,(min(gj)+max(gj))//2;oi,oj=zip(*O);oi0,oj0=min(oi),min(oj);o=[r[:]for r in g]
 for i,j in O:
  ni,nj=i-oi0+ci-1,j-oj0+cj-1
  if 0<=ni<h and 0<=nj<w:o[ni][nj]=g[i][j]
 return o
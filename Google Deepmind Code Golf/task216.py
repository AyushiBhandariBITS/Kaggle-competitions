def p(g):
 h,w=len(g),len(g[0]);s=[[0]*w for _ in g];C=[]
 for i in range(h):
  for j in range(w):
   if g[i][j]and not s[i][j]:
    q=[(i,j)];s[i][j]=1;c=[]
    while q:
     x,y=q.pop(0);c+=[(x,y)]
     for dx,dy in((1,0),(-1,0),(0,1),(0,-1)):
      X,Y=x+dx,y+dy
      if 0<=X<h and 0<=Y<w and not s[X][Y]and g[X][Y]:s[X][Y]=1;q+=[(X,Y)]
    C+=[c]
 if not C:return[g[i][:]for i in range(h)]
 b=lambda c:(mi:=min(x for x,_ in c),mj:=min(y for _,y in c),ma:=max(x for x,_ in c),mb:=max(y for _,y in c))
 S=lambda c:(sum(g[i][j]==2 for i in range(b(c)[0],b(c)[2]+1)for j in range(b(c)[1],b(c)[3]+1)),-(b(c)[2]-b(c)[0]+1),-(b(c)[3]-b(c)[1]+1),-b(c)[0],-b(c)[1])
 i0,j0,i1,j1=b(max(C,key=S))
 return[r[j0:j1+1]for r in g[i0:i1+1]]
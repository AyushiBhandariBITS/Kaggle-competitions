def p(g):
 h=len(g);w=len(g[0]);v=set()
 for i in range(h):
  for j in range(w):
   if g[i][j]==1 and(i,j)not in v:
    s=[(i,j)];c=[];n=e=0;v.add((i,j))
    while s:
     y,x=s.pop();c+=[(y,x)];n+=1
     for Y,X in(y+1,x),(y-1,x),(y,x+1),(y,x-1):
      if h>Y>=0<=X<w and g[Y][X]==1:
       e+=1
       if(Y,X)not in v:v.add((Y,X));s+=[(Y,X)]
    if e>=2*n:
     for y,x in c:g[y][x]=8
 return g
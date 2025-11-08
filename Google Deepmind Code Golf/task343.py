def p(G):
 from collections import Counter
 H,W=len(G),len(G[0])
 bg=Counter(v for r in G for v in r).most_common(1)[0][0]

 def bfs(i,j):
  q=[(i,j)];s={(i,j)};c=[]
  while q:
   x,y=q.pop();c+=[(x,y,G[x][y])]
   for a,b in((1,0),(-1,0),(0,1),(0,-1)):
    X,Y=x+a,y+b
    if 0<=X<H and 0<=Y<W and (X,Y)not in s and G[X][Y]!=bg:
     s.add((X,Y));q+=[(X,Y)]
  return c

 st=None
 for i in range(H):
  for j in range(W):
   if G[i][j]!=bg:st=(i,j);break
  if st:break
 if not st:return[G[r][:]for r in G]

 o=bfs(*st)
 mi,mj=min(i for i,_,_ in o),min(j for _,j,_ in o)
 cols={}
 for i,j,c in o:cols.setdefault(j-mj,[]).append((i-mi,c))
 for k in cols:cols[k]=tuple(sorted(cols[k]))
 w=max(cols)+1
 sig=lambda j:cols.get(j,())
 p=w
 for t in range(1,w+1):
  if all(sig(x)==sig(x+t)for x in range(w-t)):p=t;break
 for i,j,c in o:
  b=j-mj
  for m in range(0,(W-mj+p-1)//p+1):
   nj=mj+b+m*p
   if 0<=nj<W:G[i][nj]=c
 return G
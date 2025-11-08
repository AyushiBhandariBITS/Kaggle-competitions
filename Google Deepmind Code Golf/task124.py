def p(g):
 from collections import Counter as C
 H,W=len(g),len(g[0])
 bg=max(C(v for r in g for v in r),key=lambda x:sum(v==x for r in g for v in r))
 o=[(i,j,g[i][j])for i in range(H)for j in range(W)if g[i][j]!=bg]
 if not o:return[[0]*W for _ in range(W)]
 mi,ma=min(i for i,_,_ in o),max(i for i,_,_ in o);h=ma-mi+1
 x={(i-mi,j):c for i,j,c in o}
 p=h
 for k in range(1,h):
  if all((i-k,j)in x or i<k for i,j in x):p=k;break
 O=[[0]*W for _ in range(W)]
 def f(d):
  for i,j,c in o:
   ii=i+d;jj=j
   if 0<=ii<W and 0<=jj<W:O[ii][jj]=c
 f(0)
 if p<h:
  for k in range(p,W,p):f(k)
 else:
  r={}
  for i,j,c in o:r.setdefault(i,[]).append((j,c))
  d=0
  if(ma-2)in r:d=min(j for j,_ in r[ma])-min(j for j,_ in r[ma-2])
  elif(ma-1)in r:d=min(j for j,_ in r[ma])-min(j for j,_ in r[ma-1])
  for y in range(ma+1,W):
   b=r.get(y-2,r.get(y-1,[]));r[y]=[]
   for j,c in b:
    jj=j+d
    if 0<=jj<W:O[y][jj]=c;r[y].append((jj,c))
 return O
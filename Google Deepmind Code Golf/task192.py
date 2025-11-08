def p(g,L=len,R=range):
 h,w=L(g),L(g[0]);f=sum(g,[]);c={v:f.count(v)for v in set(f)if v}
 if not c:return g
 P=max(c,key=lambda k:(c[k],k))
 F=[[0]*w for _ in g];S=[[0]*w for _ in g]
 for r in R(h):
  for x in R(w):
   if g[r][x]==P and not S[r][x]:
    q=[(r,x)];S[r][x]=1;r0=r1=r;c0=c1=x
    while q:
     y,x=q.pop();r0=min(r0,y);r1=max(r1,y);c0=min(c0,x);c1=max(c1,x)
     for dy,dx in((1,0),(-1,0),(0,1),(0,-1)):
      Y,X=y+dy,x+dx
      if 0<=Y<h and 0<=X<w and not S[Y][X] and g[Y][X]==P:S[Y][X]=1;q.append((Y,X))
    for Y in R(r0,r1+1):
     for X in R(c0,c1+1):F[Y][X]=1
 o=[[0]*w for _ in g]
 for r in R(h):
  for x in R(w):
   v=g[r][x]
   if v==P or(v and F[r][x]and((r>0 and g[r-1][x]==P)or(r+1<h and g[r+1][x]==P)or(x>0 and g[r][x-1]==P)or(x+1<w and g[r][x+1]==P))):o[r][x]=P
 return o
def p(g):
 h,w=len(g),len(g[0]);v=[[0]*w for _ in g];c=[]
 for y in range(h):
  for x in range(w):
   if g[y][x]==8 and not v[y][x]:
    q=[(y,x)];v[y][x]=1;s=[]
    while q:i,j=q.pop();s+=[(i,j)];[q.append((a,b)) or v.__setitem__(a,[*v[a][:b],1,*v[a][b+1:]]) for di in(-1,0,1) for dj in(-1,0,1) if di!=0 or dj!=0 for a,b in [(i+di,j+dj)] if 0<=a<h and 0<=b<w and not v[a][b] and g[a][b]==8]
    c+=[s]
 if not c:return [r[:] for r in g]
 n=lambda s:tuple(sorted((i-min(i for i,_ in s),j-min(j for _,j in s)) for i,j in s))
 d={};[d.setdefault(n(s),[]).append(s) for s in c];m=min(len(x) for x in d.values());p=[s for x in d.values() if len(x)==m for s in x];s=min(p,key=lambda s:(min(i for i,_ in s),min(j for _,j in s)))
 o=[[1 if v==8 else v for v in r] for r in g]
 for i,j in s:o[i][j]=2
 return o
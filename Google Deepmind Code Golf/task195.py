def p(g):
 h,w=len(g),len(g[0]);f=sum(g,[]);b=max(set(f),key=f.count)
 c=[(i,j)for i in range(h)for j in range(w)if g[i][j]!=b]
 if not c:return[list(r)for r in g]
 i0=min(i for i,_ in c);i1=max(i for i,_ in c);j0=min(j for _,j in c);j1=max(j for _,j in c)
 H,W=i1-i0+1,j1-j0+1;O=[[0]*W for _ in[0]*H]
 for a in range(H):
  for d in range(W):
   v1,v2=g[i0+a][j0+d],g[i0+(3*a)%H][j0+(3*d)%W]
   O[a][d]=v1*(v1==v2)
 return O
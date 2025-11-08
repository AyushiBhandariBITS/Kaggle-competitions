def p(g):
 if not g or not g[0]:return []
 h,w=len(g),len(g[0]);v=set();B=[]
 for i in range(h):
  for j in range(w):
   if(i,j)in v:continue
   c=g[i][j];s=[(i,j)];t=[]
   while s:
    x,y=s.pop();v.add((x,y));t+=[(x,y)]
    for X,Y in((1,0),(-1,0),(0,1),(0,-1)):
     a,b=x+X,y+Y
     if 0<=a<h and 0<=b<w and(a,b)not in v and g[a][b]==c:s+=[(a,b)]
   if len(t)>len(B):B=t
 I,J=zip(*B);a,b,c,d=min(I),min(J),max(I),max(J);M=[r[b:d+1]for r in g[a:c+1]]
 if not M:return []
 bg=max(set(x for r in M for x in r),key=lambda x:sum(rr.count(x)for rr in M))
 H,W=len(M),len(M[0])
 while M and sum(x==bg for x in M[0])*2<=W:M.pop(0);H-=1
 while M and sum(x==bg for x in M[-1])*2<=W:M.pop();H-=1
 if not M:return []
 C=list(zip(*M))
 while C and sum(x==bg for x in C[0])*2<=H:C.pop(0)
 while C and sum(x==bg for x in C[-1])*2<=H:C.pop()
 if not C:return []
 M=[list(r)for r in zip(*C)]
 V=[x for r in M for x in r];bg=max(set(V),key=V.count);rc=min(set(V),key=V.count)
 H,W=len(M),len(M[0]);O=[[bg]*W for _ in range(H)]
 R={i for i,r in enumerate(M)if rc in r};C={j for j in range(W)if rc in[r[j]for r in M]}
 for i in R:O[i]=[rc]*W
 for j in C:
  for i in range(H):O[i][j]=rc
 return O
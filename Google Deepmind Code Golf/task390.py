def p(g):
 G=[r[:]for r in g];h,w=len(G),len(G[0])
 P=[(i,j)for i in range(h)for j in range(w)if G[i][j]==2]
 if not P:return G
 R,C=zip(*P);t,b,l,r=min(R),max(R),min(C),max(C)
 F=[i for i in range(h)if all(G[i][c]==2 for c in range(l,r+1))]
 if F:
  T,B=min(F),max(F)
  for i in range(T+1,B):
   for j in[c for c in range(l+1,r)if G[i][c]==5]:
    G[i][j]=0;d1,d2=i-T,B-i;n=T-d1 if d1<=d2 else B+d2
    if 0<=n<h:G[n][j]=5
 else:
  for i in range(t,b+1):
   for j in[c for c in range(l+1,r)if G[i][c]==5]:
    G[i][j]=0;d1,d2=j-l,r-j;n=l-d1 if d1<=d2 else r+d2
    if 0<=n<w:G[i][n]=5
 return G
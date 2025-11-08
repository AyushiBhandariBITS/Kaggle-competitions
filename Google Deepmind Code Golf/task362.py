def p(G):
 from collections import Counter
 H,W=len(G),len(G[0]);f=[(i,j)for i in range(H)for j in range(W)if G[i][j]==5];n=len(f);v=[0if x==5 else x for r in G for x in r];c=min(Counter(v),key=v.count)
 def ok(i,j):return G[i][j]==c and all(0<=i+a<H and 0<=j+b<W and G[i+a][j+b]==c for a,b in((1,0),(-1,0),(0,1),(0,-1)))
 b=next(((i,j)for i in range(H)for j in range(W)if ok(i,j)),0)or next(((i,j)for i in range(H)for j in range(W)if G[i][j]==c),0)
 if not b:return G
 ci,cj=b[0]+n,b[1]-n;O=[[0]*W for _ in G]
 if 0<=ci<H:O[ci]=[c]*W
 if 0<=cj<W:
  for i in range(H):O[i][cj]=c
 return O
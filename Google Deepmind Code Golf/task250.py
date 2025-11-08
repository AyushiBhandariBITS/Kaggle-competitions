def p(g):
 H,W=len(g),len(g[0]);I=[r[:]for r in g]
 t2=[(i,j)for i in range(H)for j in range(W)if I[i][j]==2];t5=[(i,j)for i in range(H)for j in range(W)if I[i][j]==5]
 if not t2 or not t5:return I
 ti,tj=min(i for i,_ in t2),min(j for _,j in t2);bi,bj=max(i for i,_ in t2),max(j for _,j in t2)
 P=({(i,j)for j in range(max(0,tj-1),min(W,bj+2))for i in(ti-1,bi+1)if 0<=i<H}|{(i,j)for i in range(max(0,ti-1),min(H,bi+2))for j in(tj-1,bj+1)if 0<=j<W})
 n=lambda i,j:min(P,key=lambda x:abs(x[0]-i)+abs(x[1]-j));t={n(i,j)for i,j in t5}
 from collections import Counter;bg=max(Counter(v for r in I for v in r),key=Counter(v for r in I for v in r).get)
 for i,j in t5:I[i][j]=bg
 for i,j in t:I[i][j]=5
 return I
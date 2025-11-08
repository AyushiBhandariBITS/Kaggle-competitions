from collections import Counter
def p(g):
 I=[r[:]for r in g];H,W=len(I),len(I[0])
 a=[(i,j)for i in range(H)for j in range(W)if I[i][j]==2];b=[(i,j)for i in range(H)for j in range(W)if I[i][j]==3]
 if not a or not b:return I
 i1=min(i for i,_ in a);j1=min(j for _,j in a);i2=min(i for i,_ in b);j2=min(j for _,j in b);d1,d2=i2-i1+1,j2-j1+1
 bg=max(Counter(v for r in I for v in r),key=Counter(v for r in I for v in r).get)
 for i,j in a:I[i][j]=bg
 for i,j in a:
  u,v=i+d1,j+d2
  if 0<=u<H and 0<=v<W:I[u][v]=2
 return I
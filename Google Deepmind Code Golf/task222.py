def p(g):
 h,w=len(g),len(g[0]);b=(0,0,0,0,0,0)
 for k in range(1,10):
  H=[0]*w
  for r in range(h):
   for c in range(w):H[c]=H[c]+1 if g[r][c]==k else 0
   S=[]
   for c in range(w+1):
    v=H[c]if c<w else 0;p=c
    while S and S[-1][0]>v:
     x,q=S.pop();a=x*(c-q)
     if a>b[0]:b=(a,r-x+1,r,q,c-1,k)
     p=q
    S.append((v,p))
 if not b[0]:return[[0]*w for _ in range(h)]
 _,r0,r1,c0,c1,k=b;O=[[0]*w for _ in range(h)]
 for i in range(r0,r1+1):O[i][c0:c1+1]=[k]*(c1-c0+1)
 return O
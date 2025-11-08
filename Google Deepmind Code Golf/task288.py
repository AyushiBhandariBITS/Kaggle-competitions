from collections import Counter
def p(g):
 h,w=len(g),len(g[0])
 c=Counter(v for r in g for v in r)
 l=min(c,key=c.get)
 z=[(i-1,j) for i in range(h) for j in range(w) if g[i][j]==l]
 if not z: return [r[:] for r in g]
 ti,q,u=min(i for i,j in z),min(j for i,j in z),max(j for i,j in z)
 v=set()
 i,j=ti,q
 while 0<=i<h and 0<=j<w:v.add((i,j));i-=1;j-=1
 i,j=ti,u
 while 0<=i<h and 0<=j<w:v.add((i,j));i-=1;j+=1
 bg=max(c,key=c.get)
 o=[r[:] for r in g]
 for i,j in v:
  if 0<=i<h and 0<=j<w and o[i][j]==bg: o[i][j]=l
 return o
def p(g):
 H,W=len(g),len(g[0])
 t,l,b,r=H,W,-1,-1
 for i in range(H):
  for j in range(W):
   if g[i][j]:
    t,l,b,r=min(t,i),min(l,j),max(b,i),max(r,j)
 if b<0:return[[]]
 x=[tuple(g[i][l:r+1])for i in range(t,b+1)]
 y=[]
 for r_ in x:
  if not y or r_!=y[-1]:y+=[r_]
 z=[]
 for c in zip(*y):
  if not z or c!=z[-1]:z+=[c]
 return[list(r)for r in zip(*z)]if z else[]
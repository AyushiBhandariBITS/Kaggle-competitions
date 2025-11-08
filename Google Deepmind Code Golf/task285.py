def p(g):
 h=len(g);w=len(g[0]);s=[*map(list,g)];D=(-1,0,1)
 for a in range(h-1):
  for b in range(w-1):
   C=[(a,b),(a,b+1),(a+1,b),(a+1,b+1)];V=[g[x][y]for x,y in C]
   if len({*V})<4:continue
   E=[v and any(0<=x+i<h and 0<=y+j<w and (x+i,y+j)not in C and g[x+i][y+j]==v for i in D for j in D if i|j)for (x,y),v in zip(C,V)]
   if sum(E)!=1:continue
   t=E.index(1);K,L=C[t][0]>a,C[t][1]>b;k=V[t];q=[C[t]];G={q[0]}
   while q:
    x,y=q.pop()
    for i in D:
     for j in D:
      if i|j:
       u,v=x+i,y+j
       if 0<=u<h and 0<=v<w and g[u][v]==k and(u,v)not in G:G.add((u,v));q.append((u,v))
   for W in(0,1):
    for H in(0,1):
     d=V[W*2+H]
     if d:
      for x,y in G:
       r=x if W==K else 2*a+1-x;c=y if H==L else 2*b+1-y
       if 0<=r<h and 0<=c<w:s[r][c]=d
 return s
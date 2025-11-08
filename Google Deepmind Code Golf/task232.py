def p(m):
 for r in m:
  for j,v in enumerate(r):
   if v:
    for k in range(j+1,len(r)):r[k]=[v,5][(k-j)%2]
    break
 return m
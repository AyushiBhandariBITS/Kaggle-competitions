def p(j):
 for c in range(len(j[0])):
  for r in range(len(j)):
   if j[r][c]:break
  for k in range(r,len(j)):j[k][c]=j[r][c]
 return j
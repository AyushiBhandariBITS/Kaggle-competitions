def p(m):
 for j in range(len(m[0])):
  for i,row in enumerate(m):
   if row[j]==1: row[j]=0; m[-1][j]=1; break
 return m
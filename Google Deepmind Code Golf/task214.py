def p(g,R=range):
 A=[r[:3]for r in g]
 C=[r[::-1]for r in A[::-1]]
 for i in R(3):
  for j in R(3):
   g[i][j+4]=A[2-j][i]
   g[i][j+8]=C[i][j]
 return g
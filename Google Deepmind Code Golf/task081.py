def p(m):
 R,C=len(m),len(m[0])
 for i in range(R-1):
  for j in range(C-1):
   s=[m[i][j],m[i][j+1],m[i+1][j],m[i+1][j+1]]
   m[i][j],m[i][j+1],m[i+1][j],m[i+1][j+1]=[1 if x!=8 and s.count(8)==3 else x for x in s]
 return m
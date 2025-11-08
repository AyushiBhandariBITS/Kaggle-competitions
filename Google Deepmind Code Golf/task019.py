def p(m):
 R,C=len(m),len(m[0])
 b=[[m[i%R][j%C]for j in range(C*2)]for i in range(R*2)]
 for i,j in[(i,j)for i in range(R*2)for j in range(C*2)if b[i][j]]:
  for x,y in[(-1,-1),(-1,1),(1,-1),(1,1)]:
   if 0<=i+x<R*2and 0<=j+y<C*2and not b[i+x][j+y]:b[i+x][j+y]=8
 return b
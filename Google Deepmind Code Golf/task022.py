def p(m):
 o=[[0]*3,[0,5,0],[0]*3]
 for i in range(11):
  for j in range(11):
   if m[i][j]==5:
    for x in-1,0,1:
     for y in-1,0,1:
      if x|y and 0<=i+x<11and 0<=j+y<11and m[i+x][j+y]:o[1+x][1+y]=m[i+x][j+y]
 return o
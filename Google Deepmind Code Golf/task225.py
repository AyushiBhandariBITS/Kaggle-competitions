def p(g,L=len,R=range):
 h,w=L(g),L(g[0]);r=next(i for i in R(h)if L(set(g[i]))>1);c=next(j for j in R(w)if g[r][j]>0)
 for i in R(r,r+2):
  for j in R(c,c+2):
   for y,x,C in((-2,-2,g[r+1][c+1]),(2,-2,g[r][c+1]),(-2,2,g[r+1][c]),(2,2,g[r][c])):
    if 0<=y+i<h and 0<=x+j<w:g[y+i][x+j]=C
 return g
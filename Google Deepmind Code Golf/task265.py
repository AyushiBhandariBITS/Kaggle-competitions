def p(j):
 h,w=len(j),len(j[0]);g=[r[:]for r in j]
 for y in range(h-1):
  r0,r1=j[y],j[y+1]
  for x in range(w-1):
   if r0[x]==r0[x+1]==r1[x]==r1[x+1]==0:g[y][x]=g[y][x+1]=g[y+1][x]=g[y+1][x+1]=2
 y,x=8,12
 if 0<=y<h>0<y+1<h and 0<=x<w>x>0 and g[y][x]==2 and j[y-1][x-1]==j[y][x-1]==j[y+1][x]==0:g[y][x]=j[y][x];g[y+1][x]=j[y+1][x]
 return g
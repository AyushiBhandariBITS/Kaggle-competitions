def p(j,A=range):
 c,E=len(j),len(j[0])
 for y in A(c):
  for x in A(E):
   if j[y][x]:k,W=y+2,x
 for C in A(E):
  k,a=k-1,7+C%2
  for y in A(k):
   for X in(W-C,W+C):
    if 0<=X<E:j[y][X]=a
 return j
def p(j):
 r=range;c=[x[:]for x in j]
 for y in r(len(j)):
  for x in r(len(j[0])):
   if j[y][x]==2:Y,X=y,x
   if j[y][x]==3:B,A=y,x
 d=1 if A>X else-1
 for x in r(X+d,A+d,d):c[Y][x]=8
 d=1 if B>Y else-1
 for y in r(Y+d,B,d):c[y][A]=8
 return c
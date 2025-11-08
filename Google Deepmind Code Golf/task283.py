def p(j):
 J,L=len(j),len(j[0])
 for W in range(J):
  for l in range(L):
   if j[W][l]==5:
    c=l;E=W
    while c<L-1and j[E][c+1]==5:c+=1
    while E<J-1and j[E+1][c]==5:E+=1
    for Y in range(W,E+1):
     for X in range(l,c+1):j[Y][X]=4
    for Y in range(W+1,E):
     for X in range(l+1,c):j[Y][X]=2
    j[W][l]=j[W][c]=j[E][l]=j[E][c]=1
 return j
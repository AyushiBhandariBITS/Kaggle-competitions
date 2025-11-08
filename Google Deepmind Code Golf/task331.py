def p(j):
 for r,R in enumerate(j):
  for c,v in enumerate(R):
   if v==1:
    if r>0:j[r-1][c]=2
    if r<9:j[r+1][c]=8
    if c>0:j[r][c-1]=7
    if c<9:j[r][c+1]=6
 return j
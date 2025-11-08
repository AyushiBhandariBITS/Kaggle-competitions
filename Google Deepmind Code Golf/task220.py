def p(j):
 c={8:4,2:1,3:6};r=[x[:]for x in j]
 for y,a in enumerate(j):
  for x,v in enumerate(a):
   if v:
    for i in(-1,0,1):
     for k in(-1,0,1):
      if i|k:r[y+i][x+k]=c[v]
 return r
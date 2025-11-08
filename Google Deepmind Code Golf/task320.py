def p(j,a=range):
 p=[r[:]for r in j]
 for k in a(len(j[0])):
  w=[i for i in a(len(j))if j[i][k]]
  for i in a(len(w)//2):p[w[-1-i]][k]=8
 return p
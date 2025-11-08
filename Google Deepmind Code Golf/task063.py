def p(j):
 c=len(j);r=range;o=[x[:]for x in j];R=r(1,c-1)
 for k in r(c):
  if j[1][k]==j[-2][k]==sum(j[i][k]for i in R)==0:
   for i in R:o[i][k]=3
 for i in r(c):
  if j[i][1]==j[i][-2]==sum(j[i][k]for k in R)==0:
   for k in R:
    if not o[i][k]:o[i][k]=3
 return o
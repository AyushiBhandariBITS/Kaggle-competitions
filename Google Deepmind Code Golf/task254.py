def p(j,A=range):
 c,e=len(j),len(j[0]);k=[sum(j[l][w]>0 for l in A(c)) for w in A(e)]
 for l in A(c):
  for w in A(e):j[l][w]=0
 w=k.index(min([x for x in k if x>0]))
 for l in A(k[w]):j[-(l+1)][w]=2
 w=k.index(max(k))
 for l in A(k[w]):j[-(l+1)][w]=1
 return j
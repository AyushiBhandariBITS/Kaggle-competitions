def p(j):
 n,c=len(j),len(j[0]);E=j[0]*20
 for k in range(2,n):j[k]=[E[k-2]]*c
 return j
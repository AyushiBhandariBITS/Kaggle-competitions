def p(j,R=range):
 c=len(j);l={0,5};E=1
 for i in R(c):
  for x in R(c):
   if j[i][x] not in l and E:
    E=0;J,a=i,x;K,W=i,x
    while K<c and j[K][x] not in l:K+=1
    while W<c and j[i][W] not in l:W+=1
    k=K-i;w=W-x
 for i in R(c-k+1):
  for x in R(c-w+1):
   if j[i][x]==5:
    for u in R(k):
     for v in R(w):j[i+u][x+v]=j[J+u][a+v]
 return j
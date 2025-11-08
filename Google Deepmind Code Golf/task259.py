def p(j,A=range):
 c,e=len(j),len(j[0]);k,w,l,jj=c,0,e,0
 for a in A(c):
  for b in A(e):
   if j[a][b]>1:k=min(k,a);w=max(w,a);l=min(l,b);jj=max(jj,b)
 return [[x-(x==1)for x in r[l:jj+1]]for r in j[k:w+1]]
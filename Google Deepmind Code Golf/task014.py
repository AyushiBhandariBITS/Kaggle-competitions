def p(m):
 t=min((v for r in m for v in r if v),key=lambda v:sum(r.count(v)for r in m))
 I=[];J=[]
 for i,r in enumerate(m):
  for j,x in enumerate(r):
   if x==t:I+=[i];J+=[j]
 return [r[min(J):max(J)+1]for r in m[min(I):max(I)+1]]
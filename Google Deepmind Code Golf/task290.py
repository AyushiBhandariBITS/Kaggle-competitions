def p(j):
 j=[r for r in j if sum(r)];a=[];c=[]
 for r in j:
  for k,v in enumerate(r):
   if v:a+=[k];c+=[v]
 x,y=set(c);m,M=min(a),max(a)
 return[[{x:y,y:x}[v]for v in r[m:M+1]]for r in j]
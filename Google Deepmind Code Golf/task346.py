def p(j):
 for a in range(len(j)-2):
  for b in range(len(j[0])-2):
   e=[r[b:b+3]for r in j[a:a+3]];k=sum(e,[])
   if min(k)>0and k.count(max(set(k),key=k.count))==8:return[[e[1][1]]]
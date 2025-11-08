def Z(j,a):return len({r[a]for r in j})
def p(c):
 e=enumerate;f=Z(c,0)+Z(c,-1)<len(set(c[0]))+len(set(c[-1]))
 c=[[x*(x!=5)for x in r]for r in c]
 for i,r in e(c):
  for j,_ in e(r):c[i][j]=max(c[0][j],c[-1][j])if f else max(r[0],r[-1])
 if f:c=[[x for x in r if x>0]for r in c];c=c[:len(c[0])]
 else:c=[r for r in c if sum(r)>0];c=[r[:len(c)]for r in c]
 return c
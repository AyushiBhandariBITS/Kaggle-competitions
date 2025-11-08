def p(m):
 c={};[c.update({x:c.get(x,0)+1})for r in m for x in r if x];n=min(c,key=c.get)
 v=[(i,j)for i,r in enumerate(m)for j,x in enumerate(r)if x==n];b,k=min(x for x,_ in v),max(x for x,_ in v);l,r=min(y for _,y in v),max(y for _,y in v)
 return [m[i][l:r+1]for i in range(b,k+1)]
from collections import Counter as C
def p(g):
 h,w=len(g),len(g[0]);c=C(e for r in g for e in r);l=min(c,key=c.get);b=max(c,key=c.get);d=max((x for x in c if x!=b),key=c.get,default=b)
 for _ in'01':g=[[g[y][x]if g[y][x]==g[y][~x]else l for x in range(w)]for y in range(h)];g=list(map(list,zip(*g)))
 R=[i for i in range(h)if len(set(g[i]))>1]or range(h)
 k=[j for j in range(w)if len({r[j]for r in g})>1]or range(w)
 return[[d if g[i][j]==l else g[i][j]for j in k]for i in R]
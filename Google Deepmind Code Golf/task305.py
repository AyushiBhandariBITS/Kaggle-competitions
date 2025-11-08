def p(j):
 n=len(j);c=sorted({x for r in j for x in r if x})
 if not c:return j
 k=len(c);return[[c[(i+j)%k]for j in range(n)]for i in range(n)]
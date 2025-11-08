from collections import Counter
def p(g):
 H,W=len(g),len(g[0]);b=Counter(v for r in g for v in r).most_common(1)[0][0];c=[(i,j)for i in range(H)for j in range(W)if g[i][j]!=b]
 if not c:return [r[:]for r in g]
 pr=max((Counter(i for i,_ in c)).items(),key=lambda x:x[1])[0];pc=max((Counter(j for _,j in c)).items(),key=lambda x:x[1])[0];s=set(c);o=[[b]*W for _ in range(H)];R=[g[pr][j]for j in range(W)if(pr,j)in s];C=[g[i][pc]for i in range(H)if(i,pc)in s]
 if R:j0=min(j for j in range(W)if(pr,j)in s);L=len(R);[o[pr].__setitem__(j,R[(j-j0)%L])for j in range(W)]
 if C:i0=min(i for i in range(H)if(i,pc)in s);L=len(C);[o[i].__setitem__(pc,C[(i-i0)%L])for i in range(H)]
 return o
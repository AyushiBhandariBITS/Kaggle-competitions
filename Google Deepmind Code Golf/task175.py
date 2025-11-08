from collections import Counter
def p(g):
    n=min(len(g),len(g[0]))
    o=[[max(g[i][j],g[j][i]) for j in range(n)] for i in range(n)]
    c=Counter(v for r in o for v in r).most_common(1)[0][0]
    for i in range(n):
        for j in range(n):
            if o[i][j]==0: o[i][j]=c
        o[i][i]=o[0][0]
    return o
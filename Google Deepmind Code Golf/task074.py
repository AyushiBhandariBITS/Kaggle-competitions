def q(I):
    if not I or not I[0]: return tuple()
    H,W=len(I),len(I[0]);A=[[0 if v==9 else v for v in r] for r in I];s=min(H,W)
    M=[[max(A[i][j],A[j][i]) for j in range(s)] for i in range(s)]
    if s<=2: return tuple(map(tuple,M))
    O=[r[:] for r in M]
    for i,row in enumerate([r[2:s][::-1] for r in M[1:s]],1):
        for j,v in enumerate(row,2):
            if v: O[i][j]=v
    return tuple(map(tuple,O))
def p(g):
    cur=tuple(map(tuple,g))
    for _ in range(256):
        nxt=q(cur)
        if nxt==cur: break
        cur=nxt
    return [list(r) for r in cur]
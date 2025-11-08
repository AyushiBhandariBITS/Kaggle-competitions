def p(g):
    from collections import Counter
    H,W=len(g),len(g[0])
    bg=max(Counter(v for r in g for v in r),key=lambda x:sum(v==x for r in g for v in r))
    G=[r[:] for r in g]
    s=[(i,j,g[i][j])for i in range(H)for j in range(W)
       if g[i][j]!=bg and all((i+di<0 or i+di>=H or j+dj<0 or j+dj>=W or g[i+di][j+dj]!=g[i][j])
                              for di,dj in((1,0),(-1,0),(0,1),(0,-1)))]
    for a_i,a_j,a_c in s:
        for b_i,b_j,_ in s:
            if a_i==b_i:ci=a_i;cj=(a_j+b_j+1)//2
            elif a_j==b_j:cj=a_j;ci=(a_i+b_i+1)//2
            else:continue
            if 0<=ci<H and 0<=cj<W:G[ci][cj]=a_c
    return G
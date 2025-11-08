def p(G):
    G=[r[:]for r in G];H,W=len(G),len(G[0]);R=[i for i in range(H)if G[i][0]and all(G[i][j]==G[i][0]for j in range(W))];C=[j for j in range(W)if G[0][j]and all(G[i][j]==G[0][j]for i in range(H))];rseg=[(R[i-1]+1if i else 0,R[i])for i in range(len(R))]+([(R[-1]+1,H)]if R else [(0,H)]);cseg=[(C[i-1]+1if i else 0,C[i])for i in range(len(C))]+([(C[-1]+1,W)]if C else [(0,W)])
    for i in range(H):
        for j in range(W):
            if not G[i][j] or i in R or j in C:continue
            for ri,(rs,re) in enumerate(rseg):
                if rs<=i<re: rli=i-rs;break
            for ci,(cs,ce) in enumerate(cseg):
                if cs<=j<ce: rcj=j-cs;break
            for rs,re in rseg:
                ti=rs+rli
                if not rs<=ti<re:continue
                for cs,ce in cseg:
                    tj=cs+rcj
                    if not cs<=tj<ce or (ti==i and tj==j):continue
                    if G[ti][tj]==0: G[ti][tj]=G[i][j]
    return G
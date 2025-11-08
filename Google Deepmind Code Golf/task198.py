def p(g):
    h, w = len(g), len(g[0])
    o = [r[:] for r in g]
    s = [[False]*w for _ in range(h)]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    for i in range(h):
        for j in range(w):
            if g[i][j] != 0 or s[i][j]:
                continue
            q = [(i, j)]
            s[i][j] = True
            c = [(i, j)]
            m_i = x_i = i
            m_j = x_j = j
            while q:
                ci, cj = q.pop()
                for di, dj in dirs:
                    ni, nj = ci+di, cj+dj
                    if 0 <= ni < h and 0 <= nj < w and not s[ni][nj] and g[ni][nj] == 0:
                        s[ni][nj] = True
                        q.append((ni, nj))
                        c.append((ni, nj))
                        if ni < m_i: m_i = ni
                        if ni > x_i: x_i = ni
                        if nj < m_j: m_j = nj
                        if nj > x_j: x_j = nj
            H = x_i - m_i + 1
            W = x_j - m_j + 1
            k = 4
            if H == W and len(c) > 1 and len(c) == H*W:
                k = 3
            for ci, cj in c:
                o[ci][cj] = k
    return o
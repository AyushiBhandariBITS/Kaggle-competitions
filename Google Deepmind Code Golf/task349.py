from collections import Counter,deque
from itertools import product

def p(G):
    H,W=len(G),len(G[0])
    G=[r[:] for r in G]
    bg=Counter(v for r in G for v in r).most_common(1)[0][0]

    seen=[[0]*W for _ in range(H)]
    comps=[]
    for i in range(H):
        for j in range(W):
            if seen[i][j]: continue
            seen[i][j]=1
            c=G[i][j]
            if c==bg: continue
            q=deque([(i,j)]); cells=[(i,j)]
            while q:
                x,y=q.popleft()
                for dx,dy in product((-1,0,1),repeat=2):
                    if dx==dy==0: continue
                    nx,ny=x+dx,y+dy
                    if 0<=nx<H and 0<=ny<W and not seen[nx][ny] and G[nx][ny]==c:
                        seen[nx][ny]=1; q.append((nx,ny)); cells.append((nx,ny))
            comps.append((c,cells))

    for i in range(H):
        for j in range(W):
            if G[i][j]==9:
                for r in range(i,H):
                    if G[r][j]==bg: G[r][j]=1

    for c,cells in comps:
        if c!=9: continue
        mi,ma=min(i for i,_ in cells),max(i for i,_ in cells)
        mj,mx=min(j for _,j in cells),max(j for _,j in cells)
        k=(mx-mj+1)//2
        for t in range(1,k+1):
            top,bottom=mi-t,ma+t
            left,right=mj-t,mx+t
            if 0<=top<H:
                for y in range(max(0,left),min(W,right+1)): G[top][y]=3
            if 0<=bottom<H:
                for y in range(max(0,left),min(W,right+1)): G[bottom][y]=3
            if 0<=left<W:
                for x in range(max(0,top),min(H,bottom+1)): G[x][left]=3
            if 0<=right<W:
                for x in range(max(0,top),min(H,bottom+1)): G[x][right]=3
    return G
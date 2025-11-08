def p(g):
    from collections import Counter,deque
    h,w=len(g),len(g[0])
    bg=Counter(x for r in g for x in r).most_common(1)[0][0]
    def comp(G):
        v=[[0]*w for _ in G];R=[]
        for i in range(h):
            for j in range(w):
                if v[i][j] or G[i][j]==bg:continue
                q=deque([(i,j)]);v[i][j]=1;c=G[i][j];S=[]
                while q:
                    x,y=q.popleft();S+=[(x,y)]
                    for X,Y in((1,0),(-1,0),(0,1),(0,-1)):
                        a,b=x+X,y+Y
                        if 0<=a<h and 0<=b<w and not v[a][b] and G[a][b]==c:v[a][b]=1;q+=[(a,b)]
                R+=[(c,S)]
        return R
    P=[r[:]for r in g]
    for _ in range(20):
        T=[r[:]for r in P]
        for i in range(h):
            for j in range(w):
                if T[i][j]==3:T[i][j]=6
        one,two=set(),set()
        for c,S in comp(P):
            I,J=zip(*S);mi,ma,mj,mx=min(I),max(I),min(J),max(J);H,W=ma-mi+1,mx-mj+1
            if len(S)==H+W-1:one|=set(S)
            if H>=3 and W>=3 and any(P[i][j]==3 for i in range(mi+1,ma)for j in range(mj+1,mx)):two|=set(S)
        for i,j in two:T[i][j]=2
        for i,j in one:T[i][j]=1
        if T==P:break
        P=T
    return P
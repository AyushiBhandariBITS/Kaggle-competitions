def p(G):
    G=tuple(tuple(r) for r in G)
    o=lambda G,c:{(i,j) for i,r in enumerate(G) for j,v in enumerate(r) if v==c}
    b=lambda c:(min([i for i,_ in c]),max([i for i,_ in c]),min([j for _,j in c]),max([j for _,j in c]))
    f=lambda G,v,c:tuple(tuple(r[j] if (i,j) not in c else v for j in range(len(r))) for i,r in enumerate(G))
    vm=lambda G:tuple(tuple(reversed(r)) for r in G)
    hm=lambda G:tuple(reversed(G))
    dm=lambda G:tuple(tuple(r) for r in zip(*G))
    e=o(G,8);d=(lambda er1,er2,ec1,ec2:(er2-er1+1)>(ec2-ec1+1))(*b(e)) if e else False
    X=dm(G) if d else G
    t=o(X,2);X=vm(X) if min((j for _,j in t),default=0) else X
    e2=o(X,8);X=hm(X) if min((i for i,_ in e2),default=0) else X
    h,w=len(X),len(X[0])
    r=set((k,j) for i,j in o(X,8) for k in range(i,h))
    tr=sorted({i for i,_ in o(X,2)});iv=list(zip([0]+tr,[i-1 for i in tr]+[h-1]))
    p=set((i,j+k) for k,(a,b) in enumerate(iv) for i,j in r if a<=i<=b)
    Y=f(X,8,p)
    if min((i for i,_ in e2),default=0):Y=hm(Y)
    if min((j for _,j in t),default=0):Y=vm(Y)
    if d:Y=dm(Y)
    return [list(r) for r in Y]
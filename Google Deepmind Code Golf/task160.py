def p(j):
 from collections import Counter,deque
 h,w=len(j),len(j[0]);bg=Counter(v for r in j for v in r).most_common(1)[0][0]
 v=[[0]*w for _ in range(h)];R=[];X=[]
 for i in range(h):
  for k in range(w):
   if v[i][k]:continue
   c=j[i][k];q=deque([(i,k)]);v[i][k]=1;C=[]
   while q:
    x,y=q.popleft();C+=[(x,y)]
    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
     A,B=x+a,y+b
     if 0<=A<h and 0<=B<w and not v[A][B]and j[A][B]==c:v[A][B]=1;q.append((A,B))
   if c and len(C)==8:
    xs,ys=zip(*C)
    if max(xs)-min(xs)==max(ys)-min(ys)==2:R+=[(min(xs),min(ys))];X+=C
 for x,y in X:j[x][y]=bg
 for i,k in R:
  for a,b in((i+1,k+1),(i,k+1),(i+2,k+1),(i+1,k),(i+1,k+2)):
   if 0<=a<h and 0<=b<w:j[a][b]=2
 return j
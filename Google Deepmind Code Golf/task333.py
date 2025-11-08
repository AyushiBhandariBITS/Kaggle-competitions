from collections import*
def solve(I):
 H,W=len(I),len(I[0]);bg=Counter(v for r in I for v in r).most_common(1)[0][0]
 N=lambda i,j:[(x,y)for x,y in((i-1,j),(i+1,j),(i,j-1),(i,j+1))if 0<=x<H and 0<=y<W]
 S=[[0]*W for _ in range(H)];O=[]
 for i in range(H):
  for j in range(W):
   if S[i][j]or I[i][j]==bg:continue
   c=I[i][j];q=deque([(i,j)]);s={(i,j)};S[i][j]=1
   while q:
    x,y=q.popleft()
    for nx,ny in N(x,y):
     if not S[nx][ny]and I[nx][ny]==c:S[nx][ny]=1;q.append((nx,ny));s.add((nx,ny))
   O+=[(c,s)]
 T={(i,j)for i in range(H)for j in range(W)if I[i][j]==3}
 if not T:return[list(r)for r in I]
 bb=lambda s:(min(i for i,_ in s),max(i for i,_ in s),min(j for _,j in s),max(j for _,j in s))
 ct=lambda s:(lambda u,l,L,R:(u+(l-u)//2,L+(R-L)//2))(*bb(s))
 man=lambda a,b:min(abs(x-X)+abs(y-Y)for x,y in a for X,Y in b)
 sh=lambda s,di,dj:{(i+di,j+dj)for i,j in s}
 ln=lambda a,b:[(a[0]+k*((b[0]>a[0])-(b[0]<a[0])),a[1]+k*((b[1]>a[1])-(b[1]<a[1])))for k in range(max(abs(b[0]-a[0]),abs(b[1]-a[1]))+1)]if a!=b else[]
 D=[]
 for c,s in O:
  if c==3:continue
  A={i for i,_ in s}&{i for i,_ in T};B={j for _,j in s}&{j for _,j in T}
  if not(A or B):continue
  sc,tc=ct(s),ct(T);v=bool(B)
  a=min(s,key=lambda k:(abs((k[1]if v else k[0])-(tc[1]if v else tc[0])),abs((k[0]if v else k[1])-(sc[0]if v else sc[1]))))
  dr,dc=((1 if sc[0]<tc[0]else-1,0)if v else(0,1 if sc[1]<tc[1]else-1))
  u,vv=set(s),set(T);fs=(0,0);n=0
  while man(u,vv)>1 and n<42:n+=1;u=sh(u,dr,dc);fs=(fs[0]+dr,fs[1]+dc)
  b=(a[0]+fs[0],a[1]+fs[1])
  for i,j in ln(a,b):
   if 0<=i<H and 0<=j<W:D+=[(c,(i,j))]
 G=[list(r)for r in I]
 for c,(i,j)in D:G[i][j]=c
 return G
p=lambda g:solve(tuple(map(tuple,g)))
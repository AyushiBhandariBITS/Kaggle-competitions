from collections import*
def p(g):
 h,w=len(g),len(g[0]);B=max(Counter(v for r in g for v in r),key=lambda x:sum(r.count(x)for r in g));v=[[0]*w for _ in g];C=[]
 for i in range(h):
  for j in range(w):
   if v[i][j]or g[i][j]==B:continue
   q=deque([(i,j)]);v[i][j]=1;s={(i,j)};c=g[i][j]
   while q:
    x,y=q.popleft()
    for a,b in((1,0),(-1,0),(0,1),(0,-1)):
     X,Y=x+a,y+b
     if 0<=X<h and 0<=Y<w and not v[X][Y]and g[X][Y]==c:v[X][Y]=1;q.append((X,Y));s.add((X,Y))
   C+=s,
 F=set()
 for s in C:
  a,b=min(i for i,_ in s),min(j for _,j in s);A,B=max(i for i,_ in s),max(j for _,j in s)
  H={(i,j)for i in range(a,A+1)for j in range(b,B+1)if(i,j)not in s}
  if H:
   x1,y1=min(i for i,_ in H),min(j for _,j in H);x2,y2=max(i for i,_ in H),max(j for _,j in H);Hh=x2-x1+1;Ww=y2-y1+1
   if Hh==Ww and len(H)==Hh*Ww:F|=H
 if not F:return g
 G=[list(r)for r in g]
 for i,j in F:G[i][j]=2
 return G
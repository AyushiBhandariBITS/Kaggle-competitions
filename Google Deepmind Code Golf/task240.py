from collections import Counter
def b(g):
 h,w=len(g),len(g[0])
 if h<3or w<3or(h-1)%2or(w-1)%2:return
 H,W=(h-1)//2,(w-1)//2;c=[[0]*W for _ in[0]*H]
 for r in range(1,h,2):
  for C in range(1,w,2):
   v=g[r][C]
   if v:
    R,C=(r-1)//2,(C-1)//2
    for a in(R,H-1-R):
     for b in(C,W-1-C):c[a][b]=v
 return c
def e(c):
 if not c:return
 H,W=len(c),len(c[0]);z=c[0][0];d={}
 for r in range(H):
  for C in range(W):
   v=c[r][C]
   if v and v!=z:
    x=d.setdefault(v,[0,0,0,0,0]);x[0]+=1;x[1]|=r==0;x[2]|=C==0;x[3]|=r==1;x[4]|=C==1
 E={v:x for v,x in d.items()if x[0]>=8}
 if not E:return
 f=lambda y:(y[1][0],-y[0])
 for I in[(1,2),(3,4)]:
  G=[y for y in E.items()if any(y[1][i]for i in I)]
  if G:return max(G,key=f)[0]
def f(c,e):
 if not c:return
 H,W=len(c),len(c[0]);q=Counter(v for r in c for v in r if v);C=[v for v,k in q.items()if k>=8];o=[r[:]for r in c]
 for v in C:
  for R in(1,0):
   M,S=(H,W)if not R else(W,H)
   for i in range(M):
    L=c[i]if R else[c[r][i]for r in range(H)];A=[j for j,x in enumerate(L)if x==v]
    if len(A)<2:continue
    if v==e:
     if not any(x not in(0,e)for x in L):continue
    elif not any(x not in(0,e,v)for x in L):continue
    for a,b in zip(A,A[1:]):
     if(a,b)==(0,S-1)or any(L[j]for j in range(a+1,b)):continue
     for j in range(a+1,b):
      if R and not o[i][j]:o[i][j]=v
      elif not R and not o[j][i]:o[j][i]=v
 return o
def x(c,h,w):
 o=[[0]*w for _ in[0]*h]
 if c:
  for r,R in enumerate(c):
   for C,v in enumerate(R):
    if v:o[2*r+1][2*C+1]=v
 return o
def s(g):c=b(g);E=e(c);F=f(c,E);return x(F,len(g),len(g[0]))
def p(g):o=s(g);return o if all(isinstance(r,list)for r in o)else[list(r)for r in g]
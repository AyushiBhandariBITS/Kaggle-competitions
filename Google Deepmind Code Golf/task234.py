def p(g):
 A,B=len(g),len(g[0])
 from collections import Counter
 C=Counter(v for r in g for v in r)
 bg=max(C,key=C.get)
 L={}
 for i,r in enumerate(g):
  for j,v in enumerate(r):
   if v!=bg:L.setdefault(v,set()).add((i,j))
 if not L:return g
 def bx(S):i0=min(i for i,_ in S);i1=max(i for i,_ in S);j0=min(j for _,j in S);j1=max(j for _,j in S);return i0,i1,j0,j1
 Rv,Rb=None,None
 for v,S in L.items():
  i0,i1,j0,j1=bx(S)
  if (i1-i0+1)*(j1-j0+1)==len(S):Rv,Rb=v,(i0,i1,j0,j1);break
 if Rv is None or len(L)==1:return g
 Ov,Os=next(v for v in L if v!=Rv),L[next(v for v in L if v!=Rv)]
 M=set()
 for i,j in Os:
  if all(0<=x<A and 0<=y<B and g[x][y]==Ov for x,y in ((i-1,j-1),(i-1,j+1),(i+1,j-1),(i+1,j+1))):M.add((i,j))
 if not M:return g
 msi,mei,msj,mej=bx(M)
 bsi,bei,bsj,bej=msi-1,mei+1,msj-1,mej+1
 h=[r[:]for r in g]
 for i,j in Os:h[i][j]=bg
 rsi,rei,rsj,rej=Rb
 vm=not(bej<rsj or bsj>rej)
 di=dj=0
 bci=bsi+(bei-bsi+1)//2;bcj=bsj+(bej-bsj+1)//2
 rci=rsi+(rei-rsi+1)//2;rcj=rsj+(rej-rsj+1)//2
 if vm:di=1 if bci<rci else -1
 else:dj=1 if bcj<rcj else -1
 def adj(a,b):asi,aei,asj,aej=a;bsi,bei,bsj,bej=b;vadj=not(aej<bsj or asj>bej)and((bsi-aei)==1 or (asi-bei)==1);hadj=not(aei<bsi or asi>bei)and((bsj-aej)==1 or (asj-bej)==1);return vadj or hadj
 c=0;oi=di;oj=dj
 while not adj((bsi,bei,bsj,bej),(rsi,rei,rsj,rej)) and c<42:c+=1;bsi+=di;bei+=di;bsj+=dj;bej+=dj;oi+=di;oj+=dj
 for i in range(max(0,bsi),min(A,bei+1)):
  for j in range(max(0,bsj),min(B,bej+1)):h[i][j]=Ov
 return h
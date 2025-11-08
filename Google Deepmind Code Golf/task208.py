from collections import*
def p(g):
 H,W=len(g),len(g[0])
 c=min(Counter(v for r in g for v in r),key=Counter(v for r in g for v in r).get)
 coords=[(i,j)for i in range(H)for j in range(W)if g[i][j]==c]
 if not coords:return [r[:]for r in g]
 t,l=map(min,zip(*coords));b,r=map(max,zip(*coords))
 ih,mW=max(1,b-t-1),max(1,r-l-1)
 def ring(i,j):return all(g[i][x]==c and g[i+ih+1][x]==c for x in range(j,j+mW+2)) and all(g[y][j]==c and g[y][j+mW+1]==c for y in range(i,i+ih+2))
 tt=None
 for i in range(H-ih-1):
  for j in range(W-mW-1):
   if all(g[a][b]==0 for a in range(i+1,i+1+ih)for b in range(j+1,j+1+mW)):
    if not tt or ring(*tt) and not ring(i,j):tt=(i,j)
 if not tt:return [r[:]for r in g]
 i,j=tt;h,w=ih+2,mW+2
 o=[r[:]for r in g]
 for b in range(j,j+w):o[i][b]=o[i+h-1][b]=c
 for a in range(i,i+h):o[a][j]=o[a][j+w-1]=c
 return o
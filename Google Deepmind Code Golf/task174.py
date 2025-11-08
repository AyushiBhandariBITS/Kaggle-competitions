from collections import*
def p(g):
 h,w=len(g),len(g[0]);b=Counter(v for r in g for v in r).most_common(1)[0][0];s=[[0]*w for _ in g];d=[(-1,0),(1,0),(0,-1),(0,1),(-1,-1),(-1,1),(1,-1),(1,1)]
 for i in range(h):
  for j in range(w):
   if g[i][j]!=b and not s[i][j]:
    q=[(i,j)];c=[(i,j)];s[i][j]=1
    while q:
     x,y=q.pop()
     for dx,dy in d:
      nx,ny=x+dx,y+dy
      if 0<=nx<h and 0<=ny<w and not s[nx][ny] and g[nx][ny]==g[i][j]:s[nx][ny]=1;q.append((nx,ny));c.append((nx,ny))
    I,J=[p[0]for p in c],[p[1]for p in c];r=[g[x][min(J):max(J)+1]for x in range(min(I),max(I)+1)]
    if all(x==x[::-1]for x in r):return [list(x)for x in r]
 return [list(x)for x in g]
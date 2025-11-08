def p(a):
 n,m=len(a),len(a[0]);o=[r[:]for r in a];v=[[0]*m for _ in a];r=[]
 for i in range(n):
  for j in range(m):
   if a[i][j]==4and not v[i][j]:
    x=i
    while x+1<n and a[x+1][j]==4:x+=1;y=j
    while y+1<m and all(a[k][y+1]==4for k in range(i,x+1)):y+=1
    for p in range(i,x+1):
     for q in range(j,y+1):v[p][q]=1
    r+=[(i,j,x,y)]
 r.sort(key=lambda z:(z[2]-z[0]+1)*(z[3]-z[1]+1))
 for k,(i,j,x,y)in enumerate(r):
  for p in range(i+1,x):
   for q in range(j+1,y):o[p][q]=1+(k>0)
 return o
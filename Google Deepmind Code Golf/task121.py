def p(j):
 for a in range(1,len(j)-1):
  for b in range(1,len(j[0])-1):
   if j[a][b]==8:e=[j[a+y][b+x]for y in(-1,0,1)for x in(-1,0,1)if(y|x)and j[a+y][b+x]];r=[[j[a+y][b+x]for x in(-1,0,1)]for y in(-1,0,1)];r[1][1]=max(set(e),key=e.count);return r
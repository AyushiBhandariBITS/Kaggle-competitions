def p(m):
 R=[i for i,r in enumerate(m)if all(x==8for x in r)]
 C=[j for j in range(len(m[0]))if all(r[j]==8for r in m)]
 for(r,c),v in {(1,0):4,(0,1):2,(1,1):6,(2,1):1,(1,2):3}.items():
  for i in range(([-1]+R+[len(m)])[r]+1,([-1]+R+[len(m)])[r+1]):
   for j in range(([-1]+C+[len(m[0])])[c]+1,([-1]+C+[len(m[0])])[c+1]):
    if m[i][j]!=8:m[i][j]=v
 return m
def p(I):
 h,w=len(I),len(I[0]);O=[]
 for r in range(0,h,3):
  R=[]
  for c in range(0,w,3):
   B=[I[r+i][c+j]for i in(0,1,2)for j in(0,1,2)if I[r+i][c+j]!=5]
   R+=[max(B,key=B.count)if B else 0]
  O+=[R]
 return O
j=lambda A:[[A[r][c]for r in range(len(A))]for c in range(len(A[0]))]
def p(A):
 c,w=len(A),len(A[0])
 if w>c:return j(p(j(A)))
 k,W,l=0,c,0
 for i,r in enumerate(A):
  if r[0]==2:k=i
  if 3 in r:W,l=min(W,i),i
 if W<k:return p(A[::-1])[::-1]
 return A[:k+1]+A[W:l+1]+[[8]*w]+[[0]*w]*(c-k+W-l-3)
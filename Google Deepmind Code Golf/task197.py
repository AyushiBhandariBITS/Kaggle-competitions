def p(j):
 A=next((c for c in j if 0 not in c),None)
 if not A: return j
 c=[];[c.append(x) for x in A if x not in c]
 for E,k in enumerate(j):
  if 0 in k and any(k):
   W=[];[W.append(x) for x in k if x not in W and x]
   if len(c)==len(W):l=dict(zip(c,W));j[E]=[l[x] for x in A]
 return j
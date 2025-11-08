def p(g):
 d={k:[[],[]]for k in set(sum(g,[]))}
 for r,R in enumerate(g):
  for c,C in enumerate(R):d[C][0]+=[r];d[C][1]+=[c]
 del d[0];Z=[[ (max(X[0])-min(X[0])+1)*(max(X[1])-min(X[1])+1),k,len(X[1])] for k,X in d.items()]
 C=sorted(Z)[-1][1]
 return [[C]*2]*2
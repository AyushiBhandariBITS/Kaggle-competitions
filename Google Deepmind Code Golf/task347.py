def p(j,A=range(3)):
 for c in A:
  for E in A:j[c][E]=(j[c][E]+j[c][E+3]>0)*6
 return[r[:3]for r in j]
def p(j):
 A=(j[3][3]<1)*6
 for r in range(3):j[r][A:A+3]=j[r][3:6][::-1]
 return j
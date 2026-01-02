
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#recursive
CUT-ROD (p,n) p = input array of prices
1  if n == 0 
2    return 0 
3  q = -inf
4  for i = 1 to n  
5    q = max{q,p[i] + CUT-ROD(p,n-i)}   
6  return q
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#DP
BOTTOM-UP-CUT-ROD(p,n)  
1  let r[0:n] be a new array // will remember solution values in r
2  r[0]=0
3  for j = 1 to n // for increasing rod length j  
4    q = -inf 
5    for i = 1 to j // i is the position of the first cut 
6        q = max{q,p[i] + r[j-i]}      
7     r[j] = q // remember the solution value for length j
8   return r[n] 
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
#extended
EXTENDED-BOTTOM-UP-CUT-ROD(p,n)  
1  let r[0:n] and s[1:n] be a new array 
2  r[0]=0
3  for j = 1 to n // for increasing rod length j  
4    q = -inf 
5    for i = 1 to j // i is the position of the first cut 
6        if q < p[i] + r[j-i]
7           q = p[i] + r[j-i]
8           s[j] = i // best cut location so far for length j
9     r[j] = q // remember the solution value for length j
10   return r & s  

PRINT-CUT-ROD-SOLUTION(p,n)
1  (r,s) = EXTENDED-BOTTOM-UP-CUT-ROD(p,n)
2  while n > 0   
3    print s[n]
4    n = n - s[n]  
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::

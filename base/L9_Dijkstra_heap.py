
#Dijkstra simple
'''
Input: directed 𝐺= 𝑉,𝐸 𝑖𝑛 𝑎𝑑𝑗𝑎𝑐𝑒𝑛𝑐𝑦 𝑙𝑖𝑠𝑡 𝑟𝑒𝑝𝑟𝑒𝑠𝑒𝑛𝑡𝑎𝑡𝑖𝑜𝑛,𝑠∈𝑉, 
non-negative length 𝑙𝑒 for each edge 𝑒∈𝐸.
Postcondition: for every 𝑣∈𝑉 the value len𝑣 is the true shortest path 
distance dist(s,v).

𝑋 = {𝑠}      
l𝑒𝑛𝑠 =0, 𝑙𝑒𝑛(𝑣) = +∞ for all 𝑣≠𝑠  
//main loop
while there is an edge (𝑣,𝑤), 𝑣∈𝑋 and 𝑤∉𝑋 do:
  (𝑎,𝑏)= such an edge minimizing 𝑙𝑒𝑛(𝑣)+𝑙𝑣𝑤 
  add 𝑏 to 𝑋
  𝑙𝑒𝑛(𝑏)=𝑙𝑒𝑛(𝑎) +𝑙𝑎b
'''

#Invariant
'''
The key of a vertex 𝑤 ∈ (𝑉 −𝑋) is the minimum Dijkstra score of 
an edge with tail 𝑣 ∈ 𝑋 and head 𝑤 OR +∞ if no such edge exists.
'''


###    DIJKSTRA____HEAP  ###
𝑋 = 𝑒𝑚𝑝𝑡𝑦 𝑠𝑒𝑡; 𝐻 = 𝑒𝑚𝑝𝑡𝑦 𝑠𝑒𝑡
𝑘𝑒𝑦(s)
for every 𝑣 ≠ 𝑠 do
  𝑘𝑒𝑦(𝑣) =+∞
//use heapify  (insert all other vertices into H)
while  H is not empty do
  𝑤 = 𝑒𝑥𝑡𝑟𝑎𝑐𝑡𝑚𝑖𝑛(𝐻)
  add 𝑤 to 𝑋
  𝑙𝑒𝑛(𝑤) = 𝑘𝑒𝑦(𝑤)
//UPDATE HEAP
  foreach edge (w,𝑦) with 𝑦 ∈ 𝑉−𝑋 do: 
    DELETE 𝑦 from 𝐻
    𝑘𝑒𝑦(𝑦) = min(𝑘𝑒𝑦(𝑦),𝑙𝑒𝑛(𝑤) +𝑙𝑣𝑤)
    INSERT 𝑦 into H

"""RUNNING TIME ANALysis
What work is done for heap ops?
- (n-1) Extract mins (which triggers the heap update = delete+insert)
How many delete/insert?
- a vertex can have as many as n-1 outgoing edges (scary! That would mean nˆ2 heap operations).
True for DENSE graphs 
→i.e., many “local tournaments”- in general, much better. 
Remember we only update the key if the tail vertex has been sucked 
into X. 
- each edge only triggers at most one Delete / Insert combo 
(if v added to X first)
So: 
# of heap operations is O((n-1)+m)=O(n+m). Since we assumed that there exist all paths (from s to 
any v), ie the graph is weakly connected, we know that m dominates n. So, we can simplify O(m).
So: 
running time =  O((m+n)logn) OR, simplified under the assumption O(m*log(n)) 
"""



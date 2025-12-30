BFS(G, s)
1for each vertex u ∈ G.V – {s}
2  u.c l r = WHITE
3  u.d = ∞
4  u.π NIL
5s.c l r = GRAY
6s.d = 0
7s.π NIL
8Q = Ø
9ENQUEUE(Q, s)
10while Q ≠ Ø
11 u = DEQUEUE(Q)
12 for each vertex v in G.Adj[u] // search the neighbors of u
13   if v.c l r == WHITE // is v being discovered now ?
14   v.c l r = GRAY
15   v.d = u.d + 1
16   v.π = u
17   ENQUEUEd(Q, v) // v is now on the frontier
18 u.c l r = BLACK // u is now behind the frontier



Correctness of BFS:

To prove the correctness of  BFS, for any graph G and 
source vertex x, we need to show  v.d = d(s,v) for any vertex v.

We begin by showing, a loop invariant: at any point of the 
algorithm, it holds that: v.d >= d(s,v) for any vertex v.

LOOP INVARIANT:
it holds that v.d >= d(s,v) for any vertx v.
INITIALIZATION:
for any vertex v != s 
v.d= inf. > d(s,v)
for vertex s:
s.d = 0 = d(s,s) 
Proving v.d >= d(s,v) for any vertex v.

MAINTENANCE:
assume the hypothesis stilll holds for all vertices.
notice some vertices have now been colored gray, and their .d attribute has been 
modified.
Notice a while iteration will only modify the .d attribute of white vertices.
Consider a gray vertex u and let v be one of it.s white neighbors.
By hypothesis, u.d >= d(s,u)
By definition :
  v.d = u.d + 1
      >= d(s,u)+1
      >= d(s,v)
Appkying previous corollary:
  v.d = u.d + 1
      >= d(s,u)+1
      >= d(s,v)

Proving after awhile iteration, it still holds that v.d >= d(s,v), for any vertex v.

TERMINATION: 
After finishing the while loop, it holds that v.d >= d(s,v) for any vertex v. 

To prove the correctness of BFS, for any graph G and 
source vertex x, we need to show  
v.d = d(s,v)  for any vertex v. 
•We have shown, at any point of the algorithm, it holds that: 
v.d  d(s,v) for any vertex v. 
•Now let us prove a more precise property regarding the .d attribute.


We claim another loop invariant: at any point of the algorithm, if 
the queue, Q, contains vertices (v1,…vr) ordered such that v1 is 
the head, it holds that: 

vr.d <= v1.d +1
vi.d <= v(i+1) for i = 1,..., r - 1

Initialization: 
Queue contains only s, so statement holds. 

Loop invariant: if the queue Q=(v1,…vr), with v1 the head, it 
holds that:
vr.d <= v1.d +1
vi.d <= v(i+1) for i = 1,..., r - 1

Maintenance: 
During a while iteration, one vertex will be DEQUEUED and 
others will be ENQUEUED. Let us show DEQUEUEING maintains the loop invariant. 
After DEQUEUING, v2 becomes the head.
By hypothesis, v2.d + 1 >= v1.d + 1
                        >= vr.d
Proving the loop invariant holds.
If the queu is empty before enqueuing, the loop invariant auto holds after
ENQUEUE operation, since the queue has a single vertex.


{....}




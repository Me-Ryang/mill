N, M, V = map(int, input().split())

adjl = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    u, v = map(int, input().split())
    adjl[u].append(v)
    adjl[v].append(u)

adjl_sort = []
for lst in adjl:
    lst.sort()
    adjl_sort.append(lst)

dfs_visit = [V]
    
def dfs(V):
    visited[V] = 1
    
    for i in adjl_sort[V]:
        if visited[i] == 0:
            visited[i] = 1
            dfs_visit.append(i)
            dfs(i)

dfs(V)
print(*dfs_visit)

bfs_visit = [V]
visited = [0] * (N + 1)

def bfs(V):
   stack = []
   stack.append(V)
   visited[V] = 1
   
   while stack:
       n = stack.pop(0)
       
       for i in adjl[n]:
           if visited[i] == 0:
               visited[i] = 1
               bfs_visit.append(i)
               stack.append(i)

bfs(V)
print(*bfs_visit)   
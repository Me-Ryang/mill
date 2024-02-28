def family(s, g):
    
    if s == G:
        return visited[s]
    
    for i in rel[s]:
        if visited[i] == -1:
            visited[i] = visited[s] + 1
            family(i, g)
        
    return visited[G]
         
N = int(input())
S, G = map(int, input().split())
M = int(input())

visited = [-1] * (N + 1)
rel = [[] for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    rel[x].append(y)
    rel[y].append(x)

visited[S] = 0
    
print(family(S, G))
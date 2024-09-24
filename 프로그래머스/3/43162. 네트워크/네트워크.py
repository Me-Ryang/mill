def solution(n, computers):
    
    def dfs(node, connect, visited):
        visited[node] = 1
        for neighbor in connect[node]:
            if visited[neighbor] == 0:
                dfs(neighbor, connect, visited)
    
    connect = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                connect[i].append(j)
    
    work = 0
    visited = [0] * n
    for r in range(n):
        if visited[r] == 0:
            dfs(r, connect, visited)
            work += 1
                
    return work
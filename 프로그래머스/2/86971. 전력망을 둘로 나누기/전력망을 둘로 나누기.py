from collections import deque

def solution(n, wires):
    
    graph = [[] for _ in range(n + 1)]
    for a, b in wires:
        graph[a].append(b)
        graph[b].append(a)
        
    def bfs(start):
        visited = [0] * (n + 1)
        q = deque([start])
        visited[start] = 1
        cnt = 1
        
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    visited[i] = 1
                    q.append(i)
                    cnt += 1
        
        return cnt
        
    answer = 100
    for a, b in wires:
        graph[a].remove(b)
        graph[b].remove(a)

        answer = min(abs(bfs(a)- bfs(b)), answer)

        graph[a].append(b)
        graph[b].append(a)

    return answer
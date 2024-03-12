import sys
from collections import deque
N, K = map(int, sys.stdin.readline().split())

def bfs(N):
    q = deque()
    q.append(N)
    
    while q:
        x = q.popleft()
        
        if x == K:
            return visited[x]
        
        for dis in (x - 1, x + 1, x * 2):
            if 0 <= dis < 100001 and visited[dis] == 0:
                visited[dis] = visited[x] + 1
                q.append(dis)

visited = [0] * 100001
print(bfs(N))
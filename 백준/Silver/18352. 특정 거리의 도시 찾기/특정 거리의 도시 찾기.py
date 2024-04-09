import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())
city = [[] for _ in range(N + 1)]
visited = [0] * (N + 1)
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    city[A].append(B)

q = deque([X])
visited[X] = 1
result = []

while q:
    x = q.popleft()

    if visited[x] == K + 1:
        result.append(x)

    if visited[x] > K + 1:
        break

    for i in city[x]:
        if visited[i] == 0:
            visited[i] = visited[x] + 1
            q.append(i)

result.sort()
if len(result) == 0:
    print(-1)
else:
    for r in range(len(result)):
        print(result[r])
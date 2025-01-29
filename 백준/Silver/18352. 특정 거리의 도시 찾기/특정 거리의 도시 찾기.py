import sys
from collections import deque

N, M, K, X = map(int, sys.stdin.readline().split())

lst = [[] for _ in range(N + 1)]
for _ in range(M):
    A, B = map(int, sys.stdin.readline().split())
    lst[A].append(B)

visited = [-1] * (N + 1)
visited[X] = 0
city = []

q = deque([X])
while q:
    x = q.popleft()

    if visited[x] == K:
        city.append(x)

    if visited[x] > K:
        break

    for i in lst[x]:
        if visited[i] == -1:
            visited[i] = visited[x] + 1
            q.append(i)

city.sort()
if city:
    for i in city:
        print(i)
else:
    print(-1)
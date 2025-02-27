import heapq
import sys
input = sys.stdin.readline

def dijkstra(start):

    q = []
    dist = [INF] * (N + 1)

    heapq.heappush(q, (0, start))
    dist[start] = 0

    while q:
        time, now = heapq.heappop(q)

        if dist[now] < time:
            continue

        for i in graph[now]:
            cost = time + i[1]
            if cost < dist[i[0]]:
                dist[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    return dist

N, M, X = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

result = 0
for i in range(1, N + 1):
    go = dijkstra(i)
    back = dijkstra(X)
    result = max(result, go[X] + back[i])

print(result)
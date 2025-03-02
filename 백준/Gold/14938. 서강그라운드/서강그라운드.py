import heapq
import sys
input = sys.stdin.readline

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
graph = [[] for _ in range(n + 1)]

for _ in range(r):
    a, b, l = map(int, input().split())
    graph[a].append((b, l))
    graph[b].append((a, l))

def dijkstra(start):

    q = []
    heapq.heappush(q, (0, start))
    distance = [int(1e9)] * (n + 1)
    distance[start] = 0

    while q:
        dist, s = heapq.heappop(q)

        if distance[s] < dist: # 기존 최단 거리보다 크면 무시
            continue

        for i in graph[s]:
            cost = dist + i[1]
            if cost <= m and cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    cnt = 0
    for i in range(1, n + 1):
        if distance[i] <= m:
           cnt += items[i - 1]

    return cnt

answer = 0
for s in range(1, n + 1):
    answer = max(answer, dijkstra(s))

print(answer)
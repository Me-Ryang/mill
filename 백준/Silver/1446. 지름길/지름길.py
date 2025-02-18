import heapq
import sys
input = sys.stdin.readline

N, D = map(int, input().split())
INF = int(1e9)
graph = [[] for _ in range(D + 1)]
distance = [INF] * (D + 1)

for _ in range(N):
    s, a, l = map(int, input().split())
    if a <= D and a - s > l:
        graph[s].append((a, l))

def drive(start):

    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, s = heapq.heappop(q)
        if s == D:
            print(dist)
            break
        for i in graph[s]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
        heapq.heappush(q, (dist + 1, s + 1))

drive(0)
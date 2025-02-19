import heapq
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
INF = int(1e9)
cows = [[] for _ in range(N + 1)]
foods = [INF] * (N + 1)

for _ in range(M):
    a, b, c = map(int, input().split())
    cows[a].append((b, c))
    cows[b].append((a, c))

def cow_food(start):

    q = []
    heapq.heappush(q, (0, start))
    foods[start] = 0

    while q:
        food, loc = heapq.heappop(q)
        if loc == N:
            print(food)
            break
        for i in cows[loc]:
            cost = food + i[1]
            if cost < foods[i[0]]:
                foods[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

cow_food(1)
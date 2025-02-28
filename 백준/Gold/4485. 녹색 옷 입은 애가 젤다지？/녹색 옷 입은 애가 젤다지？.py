import heapq
import sys
input = sys.stdin.readline

def dijkstra(N, roopie, start_x, start_y):

    q = []
    heapq.heappush(q, (roopie[start_x][start_y], start_x, start_y))
    dist = [[int(1e9)] * N for _ in range(N)]
    dist[start_x][start_y] = roopie[start_x][start_y]

    while q:
        r, x, y = heapq.heappop(q)

        if x == N - 1 and y == N - 1:
            return r

        for k in range(4):
            nx = x + dr[k]
            ny = y + dc[k]
            if 0 <= nx < N and 0 <= ny < N:
                cost = r + roopie[nx][ny]
                if cost < dist[nx][ny]:
                    dist[nx][ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

idx = 1
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while True:

    N = int(input())
    if N == 0:
        break

    roopie = [list(map(int, input().split())) for _ in range(N)]
    result = dijkstra(N, roopie,0, 0)
    print(f'Problem {idx}: {result}')
    idx += 1
import heapq
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
miro = [list(input()) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def dijkstra(start_x, start_y):

    q = []
    heapq.heappush(q, (0, start_x, start_y))
    distance = [[int(1e9)] * M for _ in range(N)]
    distance[start_x][start_y] = 0

    while q:
        dist, x, y = heapq.heappop(q)

        if x == N - 1 and y == M - 1:
            return dist

        for k in range(4):
            nx = x + dr[k]
            ny = y + dc[k]
            if 0 <= nx < N and 0 <= ny < M:
                if miro[nx][ny] == '0' and dist < distance[nx][ny]:
                    heapq.heappush(q, (dist, nx, ny))
                    distance[nx][ny] = dist
                elif miro[nx][ny] == '1' and dist + 1 < distance[nx][ny]:
                    heapq.heappush(q, (dist + 1, nx, ny))
                    distance[nx][ny] = dist

print(dijkstra(0, 0))
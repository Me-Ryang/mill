import sys
from collections import deque

N, L, R = map(int, input().split())
people = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def part_visited(start_x, start_y, part):
    q = deque([(start_x, start_y)])
    visited[start_x][start_y] = part
    p_list = [(start_x, start_y)]
    p_people = people[start_x][start_y]
    p_count = 1

    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dr[k]
            ny = y + dc[k]
            if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
                if L <= abs(people[x][y] - people[nx][ny]) <= R:
                    visited[nx][ny] = part
                    q.append((nx, ny))
                    p_list.append((nx, ny))
                    p_people += people[nx][ny]
                    p_count += 1

    people_move(p_list, p_people, p_count)

def people_move(p_list, p_people, p_count):
    if p_count > 1:
        p_val = p_people // p_count
        for x, y in p_list:
            people[x][y] = p_val
    else:
        return False

day = 0
while True:
    part = 0
    visited = [[0] * N for _ in range(N)]
    no_change = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                part += 1
                if not part_visited(i, j, part):
                    no_change += 1

    if no_change == N * N:
        break
    else:
        day += 1

print(day)
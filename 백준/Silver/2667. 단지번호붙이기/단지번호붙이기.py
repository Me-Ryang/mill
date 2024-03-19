def apartment(start_x, start_y):
    visited[start_x][start_y] = cnt
    arr[start_x][start_y] = -1

    for k in range(4):
        new_x = start_x + dr[k]
        new_y = start_y + dc[k]
        if 0 <= new_x < N and 0 <= new_y < N and int(arr[new_x][new_y]) == 1 and visited[new_x][new_y] == 0:
            visited[new_x][new_y] = cnt
            arr[new_x][new_y] = -1
            apartment(new_x, new_y)

N = int(input())
arr = [list(input()) for _ in range(N)]
visited = [[0] * N for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
for i in range(N):
    for j in range(N):
        if int(arr[i][j]) == 1:
            start_x = i
            start_y = j
            cnt += 1
            apartment(start_x, start_y)

result = [0] * cnt
for i in range(cnt):
    for lst in visited:
        result[i] += lst.count(i + 1)
result.sort()

print(cnt)
for n in result:
    print(n)
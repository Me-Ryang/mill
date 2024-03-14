N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
visited = [[0] * N for _ in range(M)]

dr = [0, 1]
dc = [1, 0]

def jino(start_x, start_y):
    
    global ans
    visited[start_x][start_y] = 1
    
    if start_x == M - 1 and start_y == N - 1:
        ans = 'Yes'
        return ans
    
    for k in range(2):
        new_x = start_x + dr[k]
        new_y = start_y + dc[k]
        if 0 <= new_x < M and 0 <= new_y < N and arr[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
            visited[new_x][new_y] = 1
            jino(new_x, new_y)
    
ans = 'No'
jino(0, 0)
print(ans)
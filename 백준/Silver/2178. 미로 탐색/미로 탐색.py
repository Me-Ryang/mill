def maze(N, M):
    
    global x, y
    
    q = []
    q.append([x, y])
    visited[x][y] = 1
    
    while q:
        x, y = q.pop(0)
        
        for k in range(4):
            new_x = x + dr[k]
            new_y = y + dc[k]
            if 0 <= new_x < N and 0 <= new_y < M: 
                if arr[new_x][new_y] == 1 and visited[new_x][new_y] == 0:
                    visited[new_x][new_y] = visited[x][y] + 1
                    q.append([new_x, new_y])
                    if new_x == (N - 1) and new_y == (M - 1):
                        return visited[new_x][new_y]

N, M = map(int, input().split())
arr = [list(map(int, input())) for _ in range(N)]
visited = [[0] * M for _ in range(N)]
x, y = 0, 0

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
print(maze(N, M))
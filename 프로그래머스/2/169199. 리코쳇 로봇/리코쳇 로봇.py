# 21:15 ~

from collections import deque

def game(board, sx, sy, r, c):
    
    # 출발 지점 넣기
    q = deque()
    q.append((sx, sy, 0))
    visited = [[False] * c for _ in range(r)]
    
    # 방향 정의
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    
    while q:
        
        x, y, cnt = q.popleft()
        if board[x][y] == 'G':
            return cnt
        
        for k in range(4):
            idx = 1
            while True:
                nx = x + dr[k] * idx
                ny = y + dc[k] * idx
                if nx < 0 or nx >= r or ny < 0 or ny >= c or board[nx][ny] == 'D':
                    if visited[nx - dr[k]][ny - dc[k]] == False:
                        visited[nx - dr[k]][ny - dc[k]] = True
                        q.append((nx - dr[k], ny - dc[k], cnt + 1))
                    break
                idx += 1                       
    return -1  
    
def solution(board):
    
    r = len(board) # 행
    c = len(board[0]) # 열
    
    # 출발 지점 찾기
    start_x, start_y = 0, 0
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'R':
                start_x = i
                start_y = j
    
    answer = game(board, start_x, start_y, r, c)
    return answer
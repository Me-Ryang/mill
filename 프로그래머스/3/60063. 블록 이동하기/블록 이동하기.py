from collections import deque

def get_next_pos(pos, board):
    
    next_pos = []
    pos = list(pos) # 현재 위치 정보를 리스트로 변환
    x_1, y_1 = pos[0][0], pos[0][1]
    x_2, y_2 = pos[1][0], pos[1][1]
    
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    
    for k in range(4):
        nx_1, ny_1 = x_1 + dx[k], y_1 + dy[k]
        nx_2, ny_2 = x_2 + dx[k], y_2 + dy[k]
        # 이동하고자 하는 두 칸이 모두 비어 있다면
        if 0 <= nx_1 < len(board) and 0 <= ny_1 < len(board) and \
           0 <= nx_2 < len(board) and 0 <= ny_2 < len(board):
            if board[nx_1][ny_1] == 0 and board[nx_2][ny_2] == 0:
                next_pos.append({(nx_1, ny_1), (nx_2, ny_2)})
        
    # 현재 로봇이 가로로 놓여 있는 경우
    if x_1 == x_2:
        for i in [-1, 1]: # 위쪽으로 회전하거나, 아래쪽으로 회전
            if board[x_1 + i][y_1] == 0 and board[x_2 + i][y_2] == 0:
                next_pos.append({(x_1, y_1), (x_1 + i, y_1)})
                next_pos.append({(x_2, y_2), (x_2 + i, y_2)})
    # 현재 로봇이 세로로 놓여 있는 경우
    elif y_1 == y_2:
        for i in [-1, 1]:
            if board[x_1][y_1 + i] == 0 and board[x_2][y_2 + i] == 0:
                next_pos.append({(x_1, y_1), (x_1, y_1 + i)})
                next_pos.append({(x_2, y_2), (x_2, y_2 + i)})

    return next_pos
    
def solution(board):
    # 맵의 외곽에 벽을 두는 형태로 맵 변형
    n = len(board)
    new_board = [[1] * (n + 2) for _ in range(n + 2)]
    for i in range(n):
        for j in range(n):
            new_board[i + 1][j + 1] = board[i][j]
    
    q = deque()
    visited = []
    pos = {(1, 1), (1, 2)} # 시작 위치 설정
    q.append((pos, 0))
    visited.append(pos) # 방문 처리
    
    while q:
        
        pos, cost = q.popleft()
        
        # 로봇이 마지막 칸에 도착
        if (n, n) in pos:
            return cost
        
        # 현재 위치에서 이동할 수 있는 위치 확인
        for next_pos in get_next_pos(pos, new_board):
            # 아직 방문하지 않은 위치라면 큐에 삽입하고 방문 처리
            if next_pos not in visited:
                q.append((next_pos, cost + 1))
                visited.append(next_pos)
    
    return 0
# 19:35 ~ 

from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def wait_rule(place, p_locs):
    
    for p_loc in p_locs:
        x, y = p_loc
        q = deque()
        q.append(p_loc)
        visited = [[0] * 5 for _ in range(5)]
        visited[x][y] = 1
        while q:
            r, c = q.popleft()
            # 4방향으로 탐색
            for k in range(4):
                nr = r + dr[k]
                nc = c + dc[k]
                if 0 <= nr < 5 and 0 <= nc < 5 and abs(nr - x) + abs(nc - y) <= 2 and visited[nr][nc] == 0:
                    if place[nr][nc] == 'X': # 파티션을 만남
                        continue
                    elif place[nr][nc] == 'P': # 응시자를 만남
                        return 0
                    q.append((nr, nc))
                    visited[nr][nc] = 1
     
    return 1 

def solution(places):
    answer = []
    
    for place in places:
        p_locs = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    p_locs.append((i, j))
        # 대기실에 응시자가 한 명도 없는 경우
        if not p_locs:
            answer.append(1)
        else: # 대기실에 응시자가 있을 경우
            answer.append(wait_rule(place, p_locs))
    
    return answer
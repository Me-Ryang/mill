from collections import deque

def solution(players, m, k):
    answer = 0
    servers = deque()
    
    for player in players:
        
        for _ in range(len(servers)):
            time = servers.popleft()
            if time - 1 != 0:
                servers.append(time - 1)
        
        max_player = (len(servers) + 1) * m
        if player >= max_player and player != 0:
            
            add_server = player // m - len(servers)
            answer += add_server
            for _ in range(add_server): # 서버 증설 개수
                servers.append(k)
            
    return answer
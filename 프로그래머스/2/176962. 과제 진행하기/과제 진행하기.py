def solution(plans):
    answer = []
    
    plans.sort(key = lambda x : x[1]) # 시작시간이 빠른 순으로 정렬
    stop = [] # 시간 내에 다 못한 과제
    
    current = 0 # 현재 시간
    for i in range(len(plans)):
        name, start, playtime = plans[i]
        start = start.split(':')
        start_time = int(start[0]) * 60 + int(start[1]) # 시간을 분으로 통일
        
        if current > start_time:
            stop.append((plans[i - 1][0], current - start_time))
        
        elif current <= start_time and i != 0:
            answer.append(plans[i - 1][0])
            if stop:
                play = start_time - current
                while play > 0 and stop:
                    s = stop.pop()
                    if s[1] <= play:
                        answer.append(s[0])
                        play -= s[1]
                    else:
                        stop.append((s[0], s[1] - play))
                        play = 0
            
        current = start_time + int(playtime)
        if i == len(plans) - 1:
            answer.append(name)
    
    while stop:
        x = stop.pop()
        answer.append(x[0])
        
    return answer
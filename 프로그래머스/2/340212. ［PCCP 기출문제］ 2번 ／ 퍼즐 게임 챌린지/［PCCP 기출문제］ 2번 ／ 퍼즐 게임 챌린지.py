def solution(diffs, times, limit):
    
    answer = 0
    start, end = min(diffs), max(diffs)
    
    while start <= end:
        
        cur_time = 0
        mid = (start + end) // 2 # 숙련도
        
        for i in range(len(diffs)):
            
            if cur_time > limit: # 제한 시간 내에 모든 퍼즐을 완성하지 못할 때
                break
            
            if diffs[i] <= mid:
                cur_time += times[i]
            elif diffs[i] > mid:
                wrong = diffs[i] - mid
                cur_time += (times[i - 1] + times[i]) * wrong + times[i]
        
        if cur_time <= limit:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    
    return answer
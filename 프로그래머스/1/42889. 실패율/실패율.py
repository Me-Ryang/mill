# 22:00 ~ -> 27개 테스트케이스 중 8개 런타임에러

def solution(N, stages):
    answer = [0] * N
    fail = [0] * (N + 1)
    
    for stage in stages:
        fail[stage - 1] += 1
    
    for i in range(N):
        x = sum(fail[:i])
        if sum(fail) - x > 0:
            answer[i] = (fail[i] / (sum(fail) - x), i + 1)
        else:
            answer[i] = (0, i + 1)
    
    sort_answer = sorted(answer, key=lambda x: (-x[0], x[1]))
    
    result = []
    for ans in sort_answer:
        result.append(ans[1])
        
    return result
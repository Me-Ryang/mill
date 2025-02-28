import heapq

def solution(n, k, enemy):
    
    answer = 0
    q = []
    
    for e in enemy:
        n -= e
        heapq.heappush(q, -e)
        if n < 0:
            if k < 1:
                break
            else:
                k -= 1
                num = heapq.heappop(q)
                n += -num
        answer += 1
                        
    return answer
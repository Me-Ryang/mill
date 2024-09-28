from collections import deque
answer = 0

def solution(numbers, target):
    
    def dfs(i, s_num):
        
        global answer
        
        if i == len(numbers):
            if s_num == target:
                answer += 1
            return
        
        dfs(i + 1, s_num + numbers[i])
        dfs(i + 1, s_num - numbers[i])
        
    dfs(0, 0)
        
    return answer
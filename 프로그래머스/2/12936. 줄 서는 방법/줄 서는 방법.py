# 21:05 ~ => 시간초과

def factorial(n):
    
    if n <= 1:
        return 1
    return factorial(n - 1) * n

def solution(n, k):
    
    answer = []
    nums = [i for i in range(1, n + 1)]
    
    while nums:
            
        # 맨 앞 숫자를 기준으로 만들 수 있는 경우의 수
        cnt = factorial(n - 1)
        # 맨 앞 숫자를 계산
        start = (k - 1) // cnt
        
        num = nums.pop(start)
        answer.append(num)
        n -= 1
        k %= cnt
    
    return answer
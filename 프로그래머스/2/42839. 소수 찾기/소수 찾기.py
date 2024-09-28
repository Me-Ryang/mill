# 소수는 어떤 수? 1과 자기자신만 약수로 가지는 수
# 0과 1은 소수가 아님

def solution(numbers):
    answer = 0
    num_list = list(numbers)
    visited = [0] * len(num_list)
    num_all = set()
    
    def make_num(i, s_num):
          
        if 0 < i <= len(num_list) and int(s_num) > 1: 
            num_all.add(int(s_num))
        
        for r in range(len(num_list)):
            if visited[r] == 0:
                visited[r] = 1
                make_num(i + 1, s_num + num_list[r])
                visited[r] = 0
    
    make_num(0, '')
    
    for num in num_all:
        answer += 1
        for i in range(2, num):
            if num % i == 0:
                answer -= 1
                break

    return answer
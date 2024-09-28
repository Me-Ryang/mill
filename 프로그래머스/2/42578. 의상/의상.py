from collections import defaultdict

def solution(clothes):
    answer = 1
    type_count = defaultdict(int)
    
    for cloth in clothes:
        type_count[cloth[1]] += 1
    
    for count in type_count.values():
        answer *= (count + 1) 

    return answer - 1
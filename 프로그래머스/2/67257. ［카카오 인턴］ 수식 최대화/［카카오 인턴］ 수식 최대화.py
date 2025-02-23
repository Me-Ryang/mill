# 00:55 ~

from itertools import permutations
from copy import deepcopy

def express_rank(rank, q):
    
    loc = 0
    
    while loc < len(rank):
        
        now = rank[loc]
        n = q.count(now)
        
        for i in range(n):
            idx = q.index(now)
            val = express_cal(now, q[idx - 1], q[idx + 1])
            # 계산한 숫자와 수식 제거
            q.pop(idx - 1)
            q.pop(idx - 1)
            q.pop(idx - 1)
            # 계산한 값 대입
            q.insert(idx - 1, val)
            
        loc += 1
       
    return abs(q[0])
            
def express_cal(now, a, b):
    
    if now == '+':
        return a + b
    elif now == '-':
        return a - b
    else:
        return a * b
    

def solution(expression):

    cal = [] # 연산자의 종류 확인
    list_express = []
    
    num = ''
    for i in expression:
        if i not in ('+', '-', '*'):
            num += i
        else:
            if i not in cal:
                cal.append(i)
            list_express.append(int(num))
            list_express.append(i)
            num = ''
    list_express.append(int(num))
    
    max_val = 0
    for rank in list(permutations(cal, len(cal))): # 연산자의 우선순위 순열
        new_express = deepcopy(list_express)
        max_val = max(max_val, express_rank(rank, new_express))
    
    return max_val
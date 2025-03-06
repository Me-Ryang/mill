import math

def solution(w,h):
    # 전체 면적
    answer = w * h
    
    # 겹치는 격자점의 수
    cnt = math.gcd(w, h)
    
    return answer - (w + h - cnt)
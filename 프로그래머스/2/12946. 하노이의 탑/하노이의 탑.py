# 20:39 ~

def hanoi(n, start, end, via, result):
    if n == 1:
        result.append([start, end])
        return
    hanoi(n - 1, start, via, end, result) # 1단계: n - 1개의 원반을 보조 기둥(via)로 이동
    result.append([start, end]) # 2단계: 가장 큰 원반을 목표 기둥(end)으로 이동
    hanoi(n - 1, via, end, start, result) # 3단계: n - 1개의 원반을 목표 기둥(end)으로 이동

def solution(n):
    result = []
    hanoi(n, 1, 3, 2, result)
    return result
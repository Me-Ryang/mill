def solution(a):
    answer = set()
    left, right = 1000000001, 1000000001
    for i in range(len(a)):
        if a[i] < left:
            left = a[i]
            answer.add(a[i])
        if a[-1-i] < right:
            right = a[-1-i]
            answer.add(a[-1-i])
        
    return len(answer)
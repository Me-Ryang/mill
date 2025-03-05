# 12:43 ~

def solution(k, ranges):
    answer = []
    n = 0
    # 숫자의 변화를 담기
    num = [k]
    
    while True:
        
        if k == 1:
            break
            
        if k % 2 == 0:
            k //= 2
        else:
            k = k * 3 + 1
        n += 1
        num.append(k)
        
    # 넓이 계산해서 저장하기
    areas = []
    for i in range(len(num) - 1):
        area = round((num[i] + num[i + 1]) / 2, 1)
        areas.append(area)
    
    for x, y in ranges:
        if x == 0 and y == 0:
            answer.append(round(sum(areas), 1))
        else:
            y += n
            if x > y:
                answer.append(-1.0)
                continue
            answer.append(round(sum(areas[x:y]), 1))

    return answer
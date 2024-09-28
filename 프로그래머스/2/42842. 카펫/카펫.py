def solution(brown, yellow):
    answer = []
    area = brown + yellow
    # x * y = area # x: 가로, y: 세로
    # (x - 2) * (y - 2) = yellow
    length = (brown // 2) + 2
    # # xy - 2(x + y) + 4 = yellow
    # # area - 2(x + y) + 4 = yellow
    # # 2(x + y) = area + 4 - yellow = brown + 4
    # x + y = round
    for x in range(1, 2000000):
        y = length - x
        if x * y == area:
            answer.extend([x, y])
            break
    answer.sort(reverse=True)
    return answer
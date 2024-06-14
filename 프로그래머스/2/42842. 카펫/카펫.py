def solution(brown, yellow):
    area = brown + yellow
    for y in range(3, area):
        if area % y == 0:
            x = area // y
            if (x - 2) * (y - 2) == yellow:
                return [x, y]
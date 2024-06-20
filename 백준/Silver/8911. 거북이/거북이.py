import copy

T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
dir = 0

for _ in range(T):
    start = [0, 0]
    end = [[0, 0]]
    move = input()
    for m in move:
        if m == 'F':
            start[0] += dx[dir]
            start[1] += dy[dir]
            end.append(copy.deepcopy(start))
        elif m == 'B':
            start[0] -= dx[dir]
            start[1] -= dy[dir]
            end.append(copy.deepcopy(start))
        elif m == 'L':
            dir = (dir - 1) % 4
        elif m == 'R':
            dir = (dir + 1) % 4

    max_x = max(end, key=lambda x: x[0])[0]
    min_x = min(end, key=lambda x: x[0])[0]
    max_y = max(end, key=lambda x: x[1])[1]
    min_y = min(end, key=lambda x: x[1])[1]

    row = abs(max_x - min_x)
    col = abs(max_y - min_y)
    print(row * col)
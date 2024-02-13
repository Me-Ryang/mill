def is_valid(nx, ny):
    return 0 <= nx < H and 0 <= ny < W

def game(s, mp, x, y):

    # U
    if s == "U":
        mp[x][y] = "^"
        if is_valid(x-1, y) and mp[x-1][y] == ".":
            mp[x][y], mp[x-1][y] = mp[x-1][y], mp[x][y]
            x, y = x-1, y
    
    # D
    if s == "D":
        mp[x][y] = "v"
        if is_valid(x+1, y) and mp[x+1][y] == ".":
            mp[x][y], mp[x+1][y] = mp[x+1][y], mp[x][y]
            x, y = x+1, y
    
    # L
    if s == "L":
        mp[x][y] = "<"
        if is_valid(x, y-1) and mp[x][y-1] == ".":
            mp[x][y], mp[x][y-1] = mp[x][y-1], mp[x][y]
            x, y = x, y-1

    # R
    if s == "R":
        mp[x][y] = ">"
        if is_valid(x, y+1) and mp[x][y+1] == ".":
            mp[x][y], mp[x][y+1] = mp[x][y+1], mp[x][y]
            x, y = x, y+1

    # S
    if s == "S":
        if mp[x][y] == "^":
            for i in range(x, -1, -1):
                if is_valid(i, y):
                    if mp[i][y] == "#":
                        break
                    if mp[i][y] == '*':
                        mp[i][y] = '.'
                        break
        elif mp[x][y] == "v":
            for i in range(x, N):
                if is_valid(i, y):
                    if mp[i][y] == "#":
                        break
                    if mp[i][y] == '*':
                        mp[i][y] = '.'
                        break
        elif mp[x][y] == ">":
            for i in range(y, N):
                if is_valid(x, i):
                    if mp[x][i] == "#":
                        break
                    if mp[x][i] == '*':
                        mp[x][i] = '.'
                        break
        elif mp[x][y] == "<":
            for i in range(y, -1, -1):
                if is_valid(x, i):
                    if mp[x][i] == "#":
                        break
                    if mp[x][i] == '*':
                        mp[x][i] = '.'
                        break
    return x, y


T = int(input())
for t in range(T):
    H, W = map(int, input().split())
    mp = [list(map(str, input())) for _ in range(H)]
    N = int(input())
    command = input()
    for i in range(H):
        for j in range(W):
            if mp[i][j] == "^" or mp[i][j] == "v" or mp[i][j] == "<" or mp[i][j] ==">":
                x, y = i, j
    
    for i in command:
        x, y = game(i, mp, x, y)
    
    print(f"#{t+1}", end=" ")
    for j in mp:
       print("".join(j))


def is_valid(nx, ny):
    return 0 <= nx < 4 and 0 <= ny < 4

def dfs(string, x, y):

    if len(str(string)) == 7:
        result.add(string)
        return
    
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if not is_valid(nx, ny):
            continue

        new_string = str(string) + str(mp[nx][ny])
        dfs(new_string, nx, ny)

T = int(input())
for t in range(T):
    mp = [list(map(int, input().split())) for _ in range(4)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = set()

    for i in range(4):
        for j in range(4):
            dfs(mp[i][j], i, j)
    
    print(f"#{t+1}", len(result))
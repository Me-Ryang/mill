def password(x, idx):

    if x == L:
        con, vow = 0, 0
        for p in cipher:
            if p in 'aeiou':
                vow += 1
            else:
                con += 1
        if vow >= 1 and con >= 2:
            print(''.join(cipher))
        return

    for i in range(idx, C):
        if visited[i] == 0:
            cipher.append(string[i])
            visited[i] = 1
            password(x + 1, i + 1)
            visited[i] = 0
            cipher.pop()

L, C = map(int, input().split())
string = list(input().split())
string.sort()
cipher = []
visited = [0 for _ in range(C)]
password(0, 0)
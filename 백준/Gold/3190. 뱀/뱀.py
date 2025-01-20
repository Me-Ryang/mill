N = int(input())
game = [[0] * N for _ in range(N)]
game[0][0] = 1
head_r, head_c = 0, 0
tail = [(0, 0)]
K = int(input())

for _ in range(K):
    r, c = map(int, input().split())
    game[r - 1][c - 1] = 2

L = int(input())
move = []
for _ in range(L):
    sec, dir = input().split()
    move.append((int(sec), dir))

sec, dir = 0, 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

while True:
    sec += 1
    if move:
        loc = move.pop(0)
        nr = head_r + dr[dir]
        nc = head_c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N:
            if game[nr][nc] == 0:
                game[nr][nc] = 1
                tail_loc = tail.pop(0)
                game[tail_loc[0]][tail_loc[1]] = 0
                head_r, head_c = nr, nc
                tail.append((head_r, head_c))
            elif game[nr][nc] == 1:
                break
            elif game[nr][nc] == 2:
                game[nr][nc] = 1
                head_r, head_c = nr, nc
                tail.append((head_r, head_c))

            if sec == loc[0]:
                if loc[1] == 'L':
                    dir = (dir + 3) % 4
                else:
                    dir = (dir + 1) % 4
            else:
                move.insert(0, loc)
        else:
            break
    else:
        nr = head_r + dr[dir]
        nc = head_c + dc[dir]
        if 0 <= nr < N and 0 <= nc < N:
            if game[nr][nc] == 0:
                game[nr][nc] = 1
                tail_loc = tail.pop(0)
                game[tail_loc[0]][tail_loc[1]] = 0
                head_r, head_c = nr, nc
                tail.append((head_r, head_c))
            elif game[nr][nc] == 1:
                break
            elif game[nr][nc] == 2:
                game[nr][nc] = 1
                head_r, head_c = nr, nc
                tail.append((head_r, head_c))
        else:
            break

print(sec)
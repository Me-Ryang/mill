N = 5

string = [input() for _ in range(N)]

MAX = 0
for chr in string:
    col = len(chr)
    if col > MAX:
        MAX = col

tpfh = []

for j in range(MAX):
    for i in range(N):
        try:
            result = string[i][j]
            tpfh.append(result)
        except IndexError:
            continue
print(''.join(tpfh))
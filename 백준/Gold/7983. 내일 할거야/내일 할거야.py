import sys

n = int(sys.stdin.readline())
homework = []

for _ in range(n):
    d, t = map(int, sys.stdin.readline().split())
    homework.append([d, t])

homework.sort(key = lambda x:x[1], reverse = True)

ans = homework[0][1] - homework[0][0]
for i in range(1, n):
    end = homework[i][1] - homework[i][0]
    if homework[i][1] <= ans:
        ans = end
    else:
        ans -= homework[i][0]

print(ans)
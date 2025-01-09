N = int(input())
paper = [[0] * 100 for _ in range(100)]
answer = 0

for _ in range(N):
    x, y = map(int, input().split())
    for i in range(10):
        for j in range(10):
            paper[x + i][y + j] = 1

for i in range(100):
    answer += paper[i].count(1)

print(answer)
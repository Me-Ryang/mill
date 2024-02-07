lst = []
for _ in range(5):
    lst.append(list(map(int, input().split())))

score = 0
winner = 0
for i in range(5):
    a = sum(lst[i])
    if score < a:
        score = a
        winner = i + 1

print(winner, score)
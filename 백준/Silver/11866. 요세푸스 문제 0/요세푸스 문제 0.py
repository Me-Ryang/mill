N, K = map(int, input().split())

per = [i for i in range(1, N + 1)]
cnt = 0
order = '<'

while len(per) > 1:
    x = per.pop(0)
    cnt += 1
    if cnt == K:
        order += str(x) + ', '
        cnt = 0
    else:
        per.append(x)

print(order + str(per[0]) + '>')
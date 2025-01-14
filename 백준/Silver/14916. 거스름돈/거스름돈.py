n = int(input())
count = 0
ml = []

for m in range(n // 5 + 1):
    nn = n - 5 * m
    if nn // 2 != 0:
        count += nn // 2
        if nn % 2 == 0:
            ml.append(m + count)
    elif nn == 0:
        ml.append(m)
    count = 0

if ml:
    print(min(ml))
else:
    print(-1)
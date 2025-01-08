N = input()
mid = len(N) // 2
first, second = 0, 0

for i in range(len(N)):
    if i < mid:
        first += int(N[i])
    else:
        second += int(N[i])

if first == second:
    print("LUCKY")
else:
    print("READY")
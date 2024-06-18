N = int(input())
beads = list(map(int, input().split()))
total = 0
result = 0

def energy():

    global total, result

    if len(beads) == 2:
        result = max(result, total)
        return

    for i in range(1, len(beads) - 1):
        total += beads[i - 1] * beads[i + 1]
        w = beads.pop(i)
        energy()
        beads.insert(i, w)
        total -= beads[i - 1] * beads[i + 1]

energy()
print(result)
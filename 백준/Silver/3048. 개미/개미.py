N1, N2 = map(int, input().split())
ant_1 = list(input())
ant_2 = list(input())

ant_1.reverse()

T = int(input())
ant = ant_1 + ant_2

for _ in range(T):
    for idx in range(len(ant) - 1):
        if ant[idx] in ant_1 and ant[idx + 1] in ant_2:
            ant[idx], ant[idx + 1] = ant[idx + 1], ant[idx]

            if ant[idx + 1] == ant_1[-1]:
                break

print(''.join(ant))
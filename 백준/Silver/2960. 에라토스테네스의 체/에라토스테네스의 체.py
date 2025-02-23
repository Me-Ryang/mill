N, K = map(int, input().split())
is_prime = [-1] * (N + 1)
is_prime[0] = False
is_prime[1] = False
k = 0

for i in range(2, N + 1):
    if is_prime[i] == -1:
        is_prime[i] = True
        k += 1
        if k == K:
            print(i)
            break
    for j in range(i * i, N + 1, i):
        if is_prime[j] == -1:
            is_prime[j] = False
            k += 1
            if k == K:
                print(j)
                exit()
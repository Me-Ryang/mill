def check(M):

    for _ in range(N):
        if M & 0x1 == 0:
            return "OFF"
        M = M >> 1
    return "ON"

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    num = bin(M)
    print(f"#{t+1}", check(M))

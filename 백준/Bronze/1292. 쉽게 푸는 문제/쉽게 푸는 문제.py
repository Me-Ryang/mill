A, B = map(int, input().split())

lst = []
for i in range(1, 1+B):
    lst += [i]*i

ans = 0
for i in range(A-1, B):
    ans += lst[i]

print(ans)
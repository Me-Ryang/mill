N, K, T = map(int, input().split())
size = list(map(int, input().split()))
size.sort(reverse=True)

cnt = 0
stack = []

while cnt < K:
    if size and size[-1] < T:
        num = size.pop()
        stack.append(num)
    else:
        if stack:
            shark = stack.pop()
            T += shark
            cnt += 1
        else:
            break

print(T)
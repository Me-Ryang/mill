N = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_v = -int(1e9) # -가 최댓값일 경우
min_v = int(1e9)

def cal(i, data):

    global add, sub, mul, div, max_v, min_v

    if i == N:
        max_v = max(max_v, data)
        min_v = min(min_v, data)

    else:
        if add:
            add -= 1
            cal(i + 1, data + A[i])
            add += 1
        if sub:
            sub -= 1
            cal(i + 1, data - A[i])
            sub += 1
        if mul:
            mul -= 1
            cal(i + 1, data * A[i])
            mul += 1
        if div:
            div -= 1
            cal(i + 1, -(abs(data) // A[i]) if data < 0 else data // A[i])
            div += 1

cal(1, A[0])
print(max_v)
print(min_v)
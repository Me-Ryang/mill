import sys
input = sys.stdin.readline

N = int(input())
want = list(map(int, input().split()))
M = int(input())
max_val = 0
answer = 0

def cal(start, end):

    global max_val, answer

    mid = (start + end) // 2
    total = 0

    if start > end:
        return

    for i in range(N):
        if want[i] <= mid:
            total += want[i]
        else:
            total += mid

    if total > M:
        cal(start, mid - 1)
    else:
        if max_val < total:
            max_val = total
            answer = mid
        cal(mid + 1, end)

if sum(want) <= M:
    print(max(want))
else:
    cal(1, max(want))
    print(answer)
import sys
input = sys.stdin.readline

N = int(input())
liquids = list(map(int, input().split()))

left_idx = 0
right_idx = N - 1

ans = abs(liquids[left_idx] + liquids[right_idx])
ans_left = left_idx
ans_right = right_idx

while left_idx < right_idx:

    tmp = liquids[left_idx] + liquids[right_idx]
    if abs(tmp) < ans:
        ans = abs(tmp)
        ans_left = left_idx
        ans_right = right_idx

        if ans == 0:
            break

    if tmp < 0:
        left_idx += 1
    else:
        right_idx -= 1

print(liquids[ans_left], liquids[ans_right])
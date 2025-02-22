import sys
input = sys.stdin.readline

N = int(input())
nums = []

is_prime = [True] * (N + 1)
is_prime[0] = is_prime[1] = False

for i in range(2, int(N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, N + 1, i):
            is_prime[j] = False

nums = [i for i in range(2, N + 1) if is_prime[i]]

def cal_find(nums):

    start = 0
    end = 0
    current = 0
    count = 0

    while end < len(nums):
        current += nums[end]

        while current > N and start <= end:
            current -= nums[start]
            start += 1

        if current == N:
            count += 1

        end += 1

    return count

if N == 1:
    print(0)
else:
    print(cal_find(nums))
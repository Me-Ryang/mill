N = int(input())
time = list(map(int, input().split()))
time.sort()

bank = 0
wait = set()
for t in time:
    bank += t
    wait.add(bank)
print(sum(wait))
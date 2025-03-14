import sys
input = sys.stdin.readline

M = int(input())
S = set()

for _ in range(M):
    action = input().rstrip()
    if action == 'all':
        S = set(i for i in range(1, 21))
    elif action == 'empty':
        S = set()
    else:
        cal, num = action.split()
        num = int(num)
        if cal == 'add':
            S.add(num)
        elif cal == 'remove':
                S.discard(num)
        elif cal == 'check':
            if num in S:
                print(1)
            else:
                print(0)
        else:
            if num in S:
                S.remove(num)
            else:
                S.add(num)
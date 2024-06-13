import sys
sys.setrecursionlimit(10**6)

X = input()
N = len(X)

num = []
ans = []
visited = [0] * N

def big_small(n):

    if n == N:
        new = int(''.join(num))
        if new not in ans and new > int(''.join(X)):
            ans.append(new)
        return

    if n > N:
        return

    for i in range(N):
        if not visited[i]:
            num.append(X[i])
            visited[i] = 1
            big_small(n + 1)
            num.pop()
            visited[i] = 0

big_small(0)
ans.sort()
if ans:
    print(ans[0])
else:
    print(0)
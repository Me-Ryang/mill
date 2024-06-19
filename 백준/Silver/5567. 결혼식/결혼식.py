from collections import deque
n = int(input())
m = int(input())

def wedding(w):

    q = deque([w])
    invite[w] = 1

    while q:
        x = q.popleft()
        for i in friend[x]:
            if invite[i] == 0:
                invite[i] = invite[x] + 1
                q.append(i)

friend = list([] for _ in range(n + 1))
invite = [0] * (n + 1)
for i in range(m):
    r, c = map(int, input().split())
    friend[r].append(c)
    friend[c].append(r)

wedding(1)
print(invite.count(2) + invite.count(3))
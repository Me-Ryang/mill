from collections import deque

T = int(input())

for tc in range(T):
    N, M = map(int, input().split())
    prior_q = deque(list(map(int, input().split())))
    idx = deque(list(range(N)))
    ans = 0

    while prior_q:
        if prior_q[0] == max(prior_q):
            ans += 1
            if idx[0] == M:
                print(ans)
                break
            else:
                prior_q.popleft()
                idx.popleft()
        else: # prior_q[0] != max(prior_q)
            prior_q.append(prior_q.popleft())
            idx.append(idx.popleft())
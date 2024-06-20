from collections import deque

T = int(input())

for _ in range(T):
    A, B = map(int, input().split())
    visited = [0] * 10000
    visited[A] = 1

    q = deque([[A, '']])
    while q:
        n, m = q.popleft()
        if n == B:
            print(m)
            break

        for i in range(1, 5):
            if i == 1:
                new, c = (n * 2) % 10000, m + 'D'
            elif i == 2:
                new, c = (n + 9999) % 10000, m + 'S'
            elif i == 3:
                new, c = n // 1000 + (n % 1000) * 10, m + 'L'
            elif i == 4:
                new, c = (n % 10) * 1000 + (n // 10), m + 'R'

            if visited[new] == 0:
                visited[new] = 1
                q.append([new, c])
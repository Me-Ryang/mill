from collections import deque
N = int(input())
sequence = deque(map(int, input().split()))
wait = deque()
wait.append(0)

num = 1
while sequence:
    if num == sequence[0]:
        num += 1
        sequence.popleft()
    if num == wait[0]:
        num += 1
        wait.popleft()
    else:
        if sequence:
            wait.appendleft(sequence.popleft())

while wait:
    if num == wait.popleft():
        num += 1
    elif num == N + 1:
        print('Nice')
        break
    else:
        print('Sad')
        break
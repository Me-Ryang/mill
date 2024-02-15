from collections import deque

for t in range(10):
    N = int(input())
    queue = deque(map(int, input().split()))
    
    while True:
        count = 0
        for _ in range(5):
            count += 1
            check = queue.popleft() - count
            if check <= 0:
                queue.append(0)
                break
            queue.append(check)
        if check <= 0:
            break

    print(f"#{N}", " ".join(map(str, queue)))
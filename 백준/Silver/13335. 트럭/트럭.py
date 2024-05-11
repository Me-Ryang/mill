from collections import deque

n, w, L = map(int, input().split())
truck = deque(map(int, input().split()))

time = 0
bridge = deque([0] * w)
while True:
    time += 1
    if truck:
        if sum(bridge) + truck[0] <= L:
            bridge.popleft()
            bridge.append(truck.popleft())
        else:
            bridge.popleft()
            if sum(bridge) + truck[0] <= L:
                bridge.append(truck.popleft())
            else:
                bridge.append(0)
    else:
        if sum(bridge) == 0:
            break
        else:
            bridge.popleft()

print(time - 1)
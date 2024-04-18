N = int(input())
building = []
for _ in range(N):
    building.append(int(input()))

building.reverse()

cnt = 0
stack = []
stack.append(building.pop())

while building:
    if not stack:
        if building:
            stack.append(building.pop())
    elif building[-1] < stack[-1]:
        cnt += len(stack)
        stack.append(building.pop())
    else:
        stack.pop()

print(cnt)
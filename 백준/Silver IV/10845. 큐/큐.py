from collections import deque

N = int(input())

q = []
for n in range(N):
    q.append(input())

pro = deque()
for cmd in q:
    if cmd == 'front':
        if len(pro) != 0:
            print(pro[0])
        else:
            print(-1)
    elif cmd == 'back':
        if len(pro) != 0:
            print(pro[-1])
        else:
            print(-1)
    elif cmd == 'size':
        print(len(pro))
    elif cmd == 'empty':
        if len(pro) == 0:
            print(1)
        else:
            print(0)
    elif cmd == 'pop':
        if len(pro) != 0:
            result = pro.popleft()
            print(result)
        else:
            print(-1)
    else: # push
        pro.append(list(cmd.split())[1])
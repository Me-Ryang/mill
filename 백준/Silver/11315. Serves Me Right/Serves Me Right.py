T = int(input())

for i in range(T):
    E, TO = map(int, input().split())
    user, time = [], []
    max_user = 0
    all_user = set()

    for _ in range(E):
        log = input().split()
        minute = list(map(int, log[0].split(':')))
        new_time = minute[0] * 60 + minute[1]

        while time and time[0] + TO <= new_time:
            user.pop(0)
            time.pop(0)

        if log[1] == 'USER':
            if log[3] == 'LOG_IN':
                user.append(log[2])
                time.append(new_time)
                all_user.add(log[2])
            else:
                if log[2] in user:
                    idx = user.index(log[2])
                    user.pop(idx)
                    time.pop(idx)
        else:
            user = []
            time = []

        max_user = max(len(user), max_user)

    print(len(all_user), max_user)
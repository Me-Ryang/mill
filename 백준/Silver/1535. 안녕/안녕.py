N = int(input())
lose = list(map(int, input().split()))
get = list(map(int, input().split()))

strong = 100
happy = 0
max_happy = 0

def hi(i, s, h):

    global max_happy

    if s > 0:
        max_happy = max(max_happy, h)

    if i == N:
        return

    hi(i + 1, s - lose[i], h + get[i])
    hi(i + 1, s, h)

hi(0, strong, happy)
print(max_happy)
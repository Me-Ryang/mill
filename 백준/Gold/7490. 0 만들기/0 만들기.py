T = int(input())

def make_zero(i, cal):

    if i == N:
        if val(cal) == 0:
            ans.append(cal)
        return

    make_zero(i + 1, cal + '+' + str(seq[i]))
    make_zero(i + 1, cal + '-' + str(seq[i]))
    make_zero(i + 1, cal + ' ' + str(seq[i]))

def val(cal):

    s = 0
    num = ''
    before = 1  # 1: +, 2: -
    cal = cal.replace(' ', '')

    for i in cal:
        if i.isdigit():
            num += i
        else:
            if before == 1:
                s += int(num)
            elif before == 2:
                s -= int(num)
            num = ''
            if i == '+':
                before = 1
            elif i == '-':
                before = 2

    if num:
        if before == 1:
            s += int(num)
        elif before == 2:
            s -= int(num)

    return s

for _ in range(T):
    N = int(input())
    seq = list(range(1, N + 1))
    cal = str(seq[0])
    ans = []

    make_zero(1, cal)
    ans.sort()
    for res in ans:
        print(res)
    print()
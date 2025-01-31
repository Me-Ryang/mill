from collections import deque

def collect(lst):

    stack = []
    for s in lst:
        if s == '(':
            stack.append(s)
        elif s == ')':
            if not stack:
                return False
            stack.pop()
    return not stack

def process(lst):

    if not lst:
        return ''

    q = deque(lst)
    l, r = 0, 0
    count = 0

    while q:
        x = q.popleft()
        count += 1
        if x == '(':
            l += 1
        else:
            r += 1
        if l == r:
            break

    u, v = lst[:count], lst[count:]

    if collect(u):
        return u + process(v)

    new = '(' + process(v) + ')'
    new += ''.join(')' if ch == '(' else '(' for ch in u[1:-1])

    return new

def solution(p):
    if not p:
        return ''
    if collect(p):
        return p
    return process(p)

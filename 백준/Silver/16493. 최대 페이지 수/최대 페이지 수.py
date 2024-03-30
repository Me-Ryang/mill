N, M = map(int, input().split())
chapter = [list(map(int, input().split())) for _ in range(M)]

def book(i, day, page):

    if day <= N:
        page_v.add(page)

    if i == M:
        return

    book(i + 1, day, page)
    book(i + 1, day + chapter[i][0], page + chapter[i][1])

page_v = set()
book(0, 0, 0)
print(max(page_v))
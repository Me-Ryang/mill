N = int(input())
home = list(map(int, input().split()))
home.sort()

print(home[(N - 1) // 2])
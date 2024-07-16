H, W = map(int, input().split())
height = list(map(int, input().split()))

rain = 0
for i in range(1, W - 1):
    left_m = max(height[:i])
    right_m = max(height[i+1:])

    compare = min(left_m, right_m)
    if height[i] < compare:
        rain += compare - height[i]

print(rain)
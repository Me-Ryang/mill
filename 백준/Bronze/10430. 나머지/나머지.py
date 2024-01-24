num = list(map(int, input().split()))

one = num[0]
two = num[1]
three = num[2]

print((one + two) % three)
print(((one % three) + (two % three)) % three)
print((one * two) % three)
print(((one % three) * (two % three)) % three)

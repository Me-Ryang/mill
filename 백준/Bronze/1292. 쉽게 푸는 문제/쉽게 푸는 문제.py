a, b = list(map(int, input().split()))

seq = []

for i in range(1, b+1):
  for j in range(i):
    seq.append(i)

print(sum(seq[a-1:b]))
A, B = map(str, input().split())
arr = [['.'] * len(A) for _ in range(len(B))]

for a in list(A):
    if a in B:
        dup = a
        break 

idx_a = list(B).index(dup)
idx_b = list(A).index(dup)

for i in range(len(arr)):
    arr[i][idx_b] = list(B)[i]
    
arr[idx_a] = list(A)

for p in range(len(arr)):
    print(''.join(arr[p]))
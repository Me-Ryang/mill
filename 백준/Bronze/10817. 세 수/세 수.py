n_list = list(map(int, input().split()))
min_val = n_list[0]
max_val = n_list[0]

for num in n_list:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

n_list.remove(min_val)
n_list.remove(max_val)
print(n_list.pop())
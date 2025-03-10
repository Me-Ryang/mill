from collections import Counter

word = input().upper()
word_count = Counter(word)
max_val = max(word_count.values())
cnt = list(word_count.values()).count(max_val)

if cnt == 1:
    print(*[k for k, v in word_count.items() if v == max_val])
else:
    print('?')
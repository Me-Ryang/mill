from collections import Counter

N, M = map(int, input().split())
words = []
for _ in range(N):
    word = input()
    if len(word) >= M:
        words.append(word)

word_cnt = Counter(words)
word_sort = sorted(word_cnt.items(), key=lambda x : (-x[1], -len(x[0]), x[0]))

for i in range(len(word_sort)):
    print(word_sort[i][0])
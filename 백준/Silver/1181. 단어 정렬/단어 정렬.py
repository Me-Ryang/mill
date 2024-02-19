N = int(input())

word = []
for n in range(N):
    word.append(input())

word = set(word)

text = []
for txt in word:
    i, j = len(txt), txt
    text.append((i, j))
text = sorted(text)

for k in range(len(text)):
    print(text[k][1])
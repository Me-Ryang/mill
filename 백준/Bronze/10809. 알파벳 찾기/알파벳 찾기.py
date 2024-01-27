from string import ascii_lowercase
alpha_list = list(ascii_lowercase)

word = list(input())

for idx in alpha_list:
    if idx not in word:
        print(-1, end = ' ')
    else:
        print(word.index(idx), end = ' ')
sen = input()

for word in range(len(sen)):
    if word != 0 and word % 10 == 0:
        print('\n' + sen[word], end = '')
    else:
        print(sen[word], end = '')
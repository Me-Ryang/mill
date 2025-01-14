S = input()
string = ''
answer = ''
come = 0

def string_check(string, answer):

    for j in range(len(string) - 1, -1, -1):
        answer += string[j]

    return answer

for i in range(len(S)):
    if S[i] == '<' or come == 1:
        if string:
            answer = string_check(string, answer)
            string = ''
        come = 1
        answer += S[i]
        if S[i] == '>':
            come = 0
    else:
        if S[i] == ' ':
            answer = string_check(string, answer)
            answer += ' '
            string = ''
        else:
            string += S[i]

if string:
    answer = string_check(string, answer)

print(answer)
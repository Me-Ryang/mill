N = int(input())
channel = [input() for _ in range(N)]

one_idx = channel.index('KBS1')
answer = '1' * one_idx + '4' * one_idx
channel.pop(one_idx)
channel.insert(0, 'KBS1')

two_idx = channel.index('KBS2')
answer += '1' * (two_idx) + '4' * (two_idx - 1)

print(answer)
from collections import deque

def solution(begin, target, words):
    
    def bfs(start):
        
        q = deque([[start, 0]])
        visited = set()
        visited.add(start)
        
        if target not in words:
            return 0
        
        while q:
            word, cnt = q.popleft()
            if word == target:
                return cnt
            for i in range(len(word)):
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + c + word[i+1:]
                    if new_word in words and new_word not in visited:
                        q.append([new_word, cnt + 1])
                        visited.add(new_word)
                    
    return bfs(begin)
N = int(input())
num = list(range(N))
parents = [0] * N
left = [0] * N
right = [0] * N

def preorder(x):
    print(parents[x], end = '')
    if left[x] != '.':
        preorder(parents.index(left[x]))
    if right[x] != '.':
        preorder(parents.index(right[x]))

def inorder(x):
    if left[x] != '.':
        inorder(parents.index(left[x]))
    print(parents[x], end = '')
    if right[x] != '.':
        inorder(parents.index(right[x]))

def postorder(x):
    if left[x] != '.':
        postorder(parents.index(left[x]))
    if right[x] != '.':
        postorder(parents.index(right[x]))
    print(parents[x], end = '')

for i in range(N):
    parents[i] , left[i], right[i] = input().split()

preorder(0)
print()
inorder(0)
print()
postorder(0)
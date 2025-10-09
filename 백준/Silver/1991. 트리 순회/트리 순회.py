import sys

input = sys.stdin.readline

N = int(input())

tree = {}

for _ in range(N):
    tmp = input().rstrip().split()

    tree[tmp[0]] = tmp[1:]

pre = ""
inorder = ""
post = ""

def pre_dfs(i):
    global pre
    pre = pre + i
    
    left = tree[i][0]
    right = tree[i][1]

    if left != '.':
        pre_dfs(left)
    if right != '.':
        pre_dfs(right)

def in_dfs(i):
    global inorder
    
    left = tree[i][0]
    right = tree[i][1]

    if left != '.':
        in_dfs(left)

    inorder = inorder + i

    if right != '.':
        in_dfs(right)

def post_dfs(i):
    global post
    
    left = tree[i][0]
    right = tree[i][1]

    if left != '.':
        post_dfs(left)
    if right != '.':
        post_dfs(right)
    post = post + i



pre_dfs('A')
in_dfs('A')
post_dfs('A')

print(pre)
print(inorder)
print(post)
import sys

tree_type = {}

while True:
    tree = sys.stdin.readline().rstrip()
    if not tree:
        break
    
    tree = tree.rstrip()
    if tree in tree_type:
        tree_type[tree] += 1
    else:
        tree_type[tree] = 1

trees = sorted(tree_type)
all_tree = sum(tree_type.values())
for i in trees:
    per = round((tree_type[i] / all_tree) * 100, 4)
    print(f'{i} {per:.4f}')
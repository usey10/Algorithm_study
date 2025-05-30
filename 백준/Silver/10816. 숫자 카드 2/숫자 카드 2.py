import sys

N = int(sys.stdin.readline())
card = list(map(int, sys.stdin.readline().split(" ")))

card_set = {}

for k in card:
    if k in card_set:
        card_set[k] += 1
    else:
        card_set[k] = 1

M = int(sys.stdin.readline())
check = list(map(int, sys.stdin.readline().split(" ")))

result = []
card_list = set(card_set.keys())

for i in check:
    if i in card_list:
        result.append(card_set[i])
    else:
        result.append(0)


print(' '.join(str(i) for i in result))
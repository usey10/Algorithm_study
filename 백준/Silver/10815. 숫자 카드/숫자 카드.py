import sys

N = int(sys.stdin.readline())
card = set(map(int, sys.stdin.readline().rstrip().split(" ")))
M = int(sys.stdin.readline())
check_card = list(map(int, sys.stdin.readline().rstrip().split(" ")))

check = []
for i in check_card:
    if i in card:
        check.append('1')
    else:
        check.append('0')

print(" ".join(check))

import sys

a, b = map(int, sys.stdin.readline().rstrip().split())

a_set = set(map(int, sys.stdin.readline().rstrip().split()))
b_set = set(map(int, sys.stdin.readline().rstrip().split()))

result = a_set - b_set
result = sorted(result)

if result:
    print(len(result))
    print(" ".join(map(str, result)))
else:
    print(0)
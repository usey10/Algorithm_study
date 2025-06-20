import sys

N,M = map(int, sys.stdin.readline().rstrip().split(" "))

a_set = set(map(int, sys.stdin.readline().rstrip().split(" ")))
b_set = set(map(int, sys.stdin.readline().rstrip().split(" ")))

atob = set(filter(lambda x : x not in b_set, a_set))
btoa = set(filter(lambda x : x not in a_set, b_set))

print(len(atob) + len(btoa))
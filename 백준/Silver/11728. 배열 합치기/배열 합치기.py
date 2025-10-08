import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())

a_list = list(map(int, input().rstrip().split()))
b_list = list(map(int, input().rstrip().split()))

all_li = []
all_li.extend(a_list)
all_li.extend(b_list)

all_li.sort()

print(" ".join(str(i) for i in all_li))
import sys

N = int(sys.stdin.readline())

text = set([sys.stdin.readline().rstrip() for _ in range(N)])

for i in text:
    reverse = i[::-1]
    if reverse in text:
        print(len(i), i[len(i)//2])
        break
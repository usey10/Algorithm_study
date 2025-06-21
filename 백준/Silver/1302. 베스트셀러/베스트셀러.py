import sys
from collections import Counter

N = int(sys.stdin.readline())

books = [sys.stdin.readline().rstrip() for _ in range(N)]

books.sort()
count = Counter(books)

most = count.most_common(1)
print(most[0][0])
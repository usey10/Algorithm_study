import sys
from collections import deque

N = int(sys.stdin.readline())

card_final = deque(i+1 for i in range(N))
cards = deque()

while card_final:
    x = card_final.pop()
    cards.appendleft(x)

    for _ in range(x):
        i = cards.pop()
        cards.appendleft(i)

print(" ".join(map(str, cards)))
import sys
from collections import deque

N = int(sys.stdin.readline())

cards = deque([i+1 for i in range(N)])
card_set = []

while len(cards) >= 2:
    card_set.append(cards.popleft())
    cards.append(cards.popleft())

card_set.append(cards.pop())
print(" ".join(map(str, card_set)))
import sys
from collections import deque
      
N = int(sys.stdin.readline())
card = deque([i+1 for i in range(N)])

while len(card) > 1:
    card.popleft()
    a = card.popleft()
    card.append(a)

print(card[0])
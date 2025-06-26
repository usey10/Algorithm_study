import sys
from collections import deque

N = int(sys.stdin.readline())


dec = sys.stdin.readline().rstrip().split()
dect = {idx+1:x for idx,x in enumerate(dec)}

balloons = deque(i+1 for i in range(N))
pop = []

while len(balloons) > 1:
    idx = balloons.popleft()
    pop.append(idx)
    move = int(dect[idx])
    if move < 0:
        balloons.rotate(-move)
    else:
        balloons.rotate(-move+1)

pop.append(balloons.pop())
print(" ".join(map(str,pop)))
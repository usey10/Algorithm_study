import sys

L = int(sys.stdin.readline())
order = sys.stdin.readline().rstrip()

visit = set()
now_x = 0
now_y = 0
visit.add((0,0))

move = {"E":(0,-1),"W":(0,1),"S":(-1,0),"N":(1,0)}

for i in order:
    x, y = move[i]
    now_x += x
    now_y += y
    visit.add((now_x, now_y))

print(len(visit))
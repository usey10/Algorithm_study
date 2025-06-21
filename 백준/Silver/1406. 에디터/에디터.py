import sys

note_l = list(sys.stdin.readline().rstrip())
note_r = []

M = int(sys.stdin.readline().rstrip())

for i in range(M):
    order = sys.stdin.readline().rstrip()
    if order == "L":
        if note_l:
            note_r.append(note_l.pop())
    elif order == "D":
        if note_r:
            note_l.append(note_r.pop())
    elif order == "B":
        if note_l:
            note_l.pop()
    else:
        add = order.split()[-1]
        note_l.append(add)

        
print(''.join(note_l + note_r[::-1]))
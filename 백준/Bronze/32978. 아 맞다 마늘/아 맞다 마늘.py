import sys

N = int(sys.stdin.readline())

all = set(sys.stdin.readline().rstrip().split(" "))
all = sorted(all)

made = set(sys.stdin.readline().rstrip().split(" "))
made = sorted(made)

for i in range(N-1):
    if all[i] != made[i]:
        answer = all[i]
        break
    else:
        continue

print(answer if answer else all[-1])
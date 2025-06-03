import sys

N = int(sys.stdin.readline())
all_worker = {}

def worker_add(x, num):
    if x not in all_worker:
        all_worker[x] = num
    else:
        all_worker[x] += num

for i in range(N):
    morning = sys.stdin.readline().rstrip().split(" ")
    day = sys.stdin.readline().rstrip().split(" ")
    night = sys.stdin.readline().rstrip().split(" ")
    dawn = sys.stdin.readline().rstrip().split(" ")
    for j in range(len(morning)):
        if morning[j] == "-":
            continue
        else:
            worker_add(morning[j], 4)
            worker_add(day[j], 6)
            worker_add(night[j], 4)
            worker_add(dawn[j], 10)

if len(all_worker) == 0:
    print("Yes")
elif max(all_worker.values()) - min(all_worker.values()) <= 12:
    print("Yes")
else:
    print("No")
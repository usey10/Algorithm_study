import sys

N, M = map(int, sys.stdin.readline().rstrip().split(" "))

people = {}
non_people = set()

for i in range(N+M):
    t = sys.stdin.readline().rstrip()
    if t not in people:
        people[t] = 1
    else:
        people[t] += 1
        non_people.add(t)


print(len(non_people))
for i in sorted(non_people):
    print(i)
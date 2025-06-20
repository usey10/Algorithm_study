import sys

n = int(sys.stdin.readline())

for _ in range(n):
    t = sys.stdin.readline().rstrip().split()
    x = int(t.pop(0))
    army = {j:0 for j in set(t)}
    for i in t:
        army[i] += 1
    if max(army.values()) < x//2+1:
        print("SYJKGW")
    else:
        maxvalue=list(army.values()).index(max(army.values()))
        print(list(army.keys())[maxvalue])
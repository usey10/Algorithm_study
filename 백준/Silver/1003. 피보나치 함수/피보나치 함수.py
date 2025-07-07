import sys

T = int(sys.stdin.readline())

count = [(1,0), (0,1)]

for i in range(2, 41):
    b1 = count[i-1]
    b2 = count[i-2]
    temp = (b2[0]+b1[0], b2[1]+b1[1])
    count.append(temp)

for _ in range(T):
    n = int(sys.stdin.readline())

    a, b = count[n]
    print(a, b)

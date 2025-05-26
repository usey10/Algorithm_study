import sys

N = int(sys.stdin.readline())

for i in range(N):
    case = sys.stdin.readline().rstrip().split(" ")
    print(f"Case #{i+1}: {" ".join(case[::-1])}")
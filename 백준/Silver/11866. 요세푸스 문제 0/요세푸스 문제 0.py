import sys

N, K = map(int, sys.stdin.readline().rstrip().split(" "))

num = [i+1 for i in range(N)]

k = K

result = []
while num:
    while k > len(num):
        k = k - len(num)
    # print(f"순서 : {k}")
    result.append(num[k-1])
    num.remove(num[k-1])
    k += K-1
    # print(k, num)
    # print(result)
    # break

print(f"<{', '.join(str(i) for i in result)}>")
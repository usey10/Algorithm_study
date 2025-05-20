N = int(input())
same = [1, 5, 6]
else_num = {2:[2,4,8,6], 3:[3,9,7,1], 4:[4,6], 7:[7,9,3,1], 8:[8,4,2,6], 9:[9,1]}
for i in range(N):
    a, b = map(int, input().split())
    if a % 10 in same:
        print(a % 10)
    elif a % 10 == 0:
        print(10)
    else:
        print(else_num[a % 10][(b % len(else_num[a % 10]))-1])
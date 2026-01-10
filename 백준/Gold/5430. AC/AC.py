import sys

input = sys.stdin.readline

T = int(input())

for tc in range(T):
    p = input().strip()
    n = int(input())
    x = input().strip()
    x = x.replace('[', '').replace(']','')
    x_list = list(map(int, x.split(','))) if n!=0 else []


    rev = False

    error = False

    for i in p:
        if i == 'D' and x_list:
            if rev:
                x_list.pop(-1)
            else:
                x_list.pop(0)
        elif i == 'D' and not x_list:
            error = True
            break
        else:
            rev = True if not rev else False

    
    if error:
        print('error')
        continue

    if rev:
        x_list.reverse()
        print("[" + ",".join(str(k) for k in x_list) + "]")
    else:
        print("[" + ",".join(str(k) for k in x_list) + "]")
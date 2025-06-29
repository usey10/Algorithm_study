import sys

N, P = map(int, sys.stdin.readline().split())

press = {i+1:[] for i in range(N)}

count = 0

for _ in range(N):
    line, pret = map(int,sys.stdin.readline().split())
    
    if len(press[line]) == 0:
        press[line].append(pret)
        count += 1

    else:
        while press[line]:
            temp = press[line].pop()
            if temp > pret:
                count += 1
            else:
                press[line].append(temp)
                break
        
        if press[line] == []:
            press[line].append(pret)
            count += 1
        elif press[line][-1] == pret:
            pass
        else:
            press[line].append(pret)
            count += 1

print(count)
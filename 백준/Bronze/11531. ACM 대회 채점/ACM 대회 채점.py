import sys

penalty = 0
wrong = {}
answer = set()

notstop = True

while notstop:
    submit = sys.stdin.readline().rstrip().split(" ")

    if '-1' in submit:
        notstop = False
        break

    n = int(submit[0])
    p,r = submit[1], submit[2]
    

    if r == 'wrong':
        if p in wrong:
            wrong[p] += 1
        else:
            wrong[p] = 1
    else:
        if p in answer:
            continue
        else:
            penalty += n + wrong.get(p, 0)*20
            answer.add(p)
    # print(penalty, wrong, answer, notstop)


print(len(answer), penalty)
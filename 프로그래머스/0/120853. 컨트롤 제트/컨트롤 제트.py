def solution(s):
    every_num = s.split(' ')
    for i in range(len(every_num)):
        if every_num[i] == 'Z':
            every_num[i-1] = 0
            every_num[i] = 0

    return sum(int(x) for x in every_num)
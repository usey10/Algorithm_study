def solution(spell, dic):
    for i in dic:
        check = [j in i for j in spell]
        if sum(check) == len(spell):
            return 1
    return 2
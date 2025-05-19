def solution(common):
    last_num = common[-1]
    if common[2] - common[1] == common[1] - common[0]:
        return last_num + common[1] - common[0]
    else:
        return last_num * (common[1] // common[0])



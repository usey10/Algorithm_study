def solution(i, j, k):
    all_num = [str(x).count(str(k)) for x in range(i,j+1)]

    return sum(all_num)
def solution(array, n):
    answer = {abs(i-n):[] for i in array}
    for i in array:
        answer[abs(i-n)].append(i)
    return min(answer[min(answer)])
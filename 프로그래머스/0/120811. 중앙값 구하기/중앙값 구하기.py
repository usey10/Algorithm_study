def solution(array):
    n = len(array) // 2
    # print(n)
    array.sort()
    # print(array)
    return array[n]
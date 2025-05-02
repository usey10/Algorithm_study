def solution(numbers, k):
    ind = (k-1)*2 % len(numbers)
    return numbers[ind]
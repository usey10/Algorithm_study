def solution(numbers):
    k = max(numbers)
    numbers.remove(k)
    return k*max(numbers)
def solution(numbers):
    result = []
    big = 0
    index = 0
    N = range(len(numbers))
    for _ in N:
        for i in range(len(numbers)):
            if numbers[i] < 10:
                if big < numbers[i]:
                    big = numbers[i]
                    index = i
            elif numbers[i] > 10:
                if big < (numbers[i] // 10):
                    big = numbers[i]
                    index = i
        print(big)
        result.append(big)
        numbers.pop(index)
        big = 0
    print(result)

# 구현한거 문제 : 10보다 작은 건 완료 했는데, 그 이외 내용이 Sort 가 안됨..

# solution
# key 를 통한 sort 로 구현
from functools import cmp_to_key

def solution(numbers):
    def compare(x,y):
        a = int(str(x) + str(y))
        b = int(str(y)+str(x))
        return 1 if b > a else -1
    key = cmp_to_key(compare)
    numbers.sort(key=key)
    print(numbers)
    return ''.join(map(str, numbers))


if __name__ == '__main__':
    numbers = [3, 30, 34, 5, 9]
    sol = solution(numbers)
    print(sol)

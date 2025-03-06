# Prob1.
# 리스트 arr의 모든 자료에 대해서,
# 짝수 데이터들의 평균과 홀수 데이터들의 평균을 각각 계산하시오.
# 출력은 2개의 출력을 리스트로 묶어 출력하시오.

# 입출력 예시)
# arr = [1, 3, 5, 7, 9, 2, 5, 1, 4]
# 결과: [3.25, 4.8]

def solution(arr):
    sum_list = [x if x % 2 == 0 else 0 for x in arr]
    sum_list2 = [x if x % 2 != 0 else 0 for x in arr]
    y1 = 0
    y2 = 0
    for i in sum_list:
        y1 += i
    for i in sum_list2:
        y2 += i
    return [y1/len(sum_list), y2/len(sum_list2)]

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 2, 5, 1, 4]
    sol = solution(arr)
    print(sol)

## solution
# 1. 일단 문제 해석 잘못함... 인덱스 기준 짝수 데이터, 홀수 데이터 였음.
# 2. list 도 sum 을 통해 다 더할 수 있음

def solution(arr):
    even_arr = arr[1::2]
    odd_arr = arr[::2]
    even_avg = sum(even_arr) / len(even_arr)
    odd_avg = sum(odd_arr) / len(odd_arr)
    return [even_avg, odd_avg]

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9, 2, 5, 1, 4]
    sol = solution(arr)
    print(sol)
# Prob2.
# 리스트의 자료 순서를 거꾸로 변경하시오.
# 추가 리스트를 생성하지 말고, 주어진 리스트에서 in-place로 하시오.
# 
# 입출력 예시)
# arr = [1, 3, 5, 7, 9]
# 결과: [9, 7, 5, 3, 1]


# 풀이 방법 : 인덱싱이 핵심 + 어디까지 반복할건지 확인 필요


def solution(arr):
    # 5개의 자료 -> 2번 반복
    # 6개의 자료 -> 3번 반복
    N = len(arr)
    for i in range(N//2):
        arr[N-i-1], arr[i] = arr[i], arr[N-i-1] # 스와핑 진행
    return arr

# 참고
# 해당 문제는 한 줄로 간단하게 구현 가능
# -> 단, 이 경우에는 inplace 로 진행한 것이 아니기 때문에 해당 문제에서는 쓰지 않음.
# def solution(arr):
#     return arr[::-1]

if __name__ == '__main__':
    arr = [1, 3, 5, 7, 9]
    sol = solution(arr)
    print(sol)
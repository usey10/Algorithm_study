# Problem1

## 문제 설명
# 카탈랑 수는 0번, 1번, 2번, ... 순으로 아래와 같이 구성되는 수열을 의미한다.

# - 1, 1, 2, 5, 14, 42, 132, 429, 1430, 4862, … 

# 이를 점화식으로 나타내면 아래와 같다.
# 𝐶₀ = 1, 𝐶ₙ₊₁ = 𝛴ⁿᵢ₌₀ 𝐶ᵢ𝐶ₙ₋ᵢ (𝑛 ≥ 0)

# 카탈랑 수의 `n` 번째 값을 구하는 프로그램을 작성하세요.

## 입력 예시
# |입력|출력|
# |---|---|
# |0|1|
# |2|2|
# |5|42|
# |7|429|

# 모범 답안

def solution(n):
    if n == 0:
        return 1 # 종료 조건
    
    value = 0

    for i in range(n):
        value += solution(i) * solution(n-i-1)

    return value
    
# 그냥 점화식 가지고 바로 작성하면 된다.. 변형 하지 말것

if __name__ == '__main__':
    N = 4
    sol = solution(N)
    print(sol)

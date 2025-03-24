# Problem3

## 문제 설명
# 하노이의 탑은 퍼즐의 일종이다.

# 하노이의 탑 퍼즐 게임 규칙은 다음과 같다.
# - 한 번에 한 개의 원판 만 옮길 수 있다.
# - 큰 원판이 작은 원판 위에 있어서는 안된다.

# 원판의 개수 `n` 이 주어졌을 때, 가장 왼쪽 기둥으로부터 끝 기둥으로 이동하는 과정을 출력하는 프로그램을 구현하세요.

# 단, 초기에 모든 원판은 가장 큰 원판부터 순서대로 왼쪽 기둥에 위치해 있다.


## 입력 예시

# |입력|출력|
# |---|---|
# |`2`|`[[1, 2], [1, 3], [2, 3]]`|
# |`3`|`[[1, 3], [1, 2], [3, 2], [1, 3], [2, 1], [2, 3], [1, 3]]`|

# solution
def solution(n):
    def solve(n, start, end, temp):
        if n == 1:
            return [[start, end]]
        return solve(n-1, start, temp, end) + [[start, end]] + solve(n-1, temp, end, start)
    return solve(n,1,3,2)
    pass


if __name__ == '__main__':
    n = 3
    sol = solution(n)
    print(sol)
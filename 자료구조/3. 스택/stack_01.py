# Prob1.
# 스택을 이용하여 문자열 s를 뒤집기


# 입출력 예시)
# s = "zerobase"
# 결과: "esaborez"


# stack 를 사용하지 않음.
def solution(s):
    res = ""
    for j in range(len(s)):
        res += s[len(s)-j-1]
    return res

# solution
def solution(s):
    res = ""
    stack = []
    for c in s:
        stack.append(c)
    while stack:
        res += stack.pop() # pop 으로 삭제하면서 res 에 저장
    return res

## solution - 더 간단한 방식(stack 미사용)
def solution(s):
    return s[::-1]

if __name__ == '__main__':
    s = "zerobase"
    sol = solution(s)
    print(sol)

def solution(s):
    t = s.split("  ")
    result = [i.strip() for i in t if i != ""]
    N = len(result)
    sol = ""
    for i in range(N):
        sol += result[N-1-i]
        sol += " "
    sol.strip()
    return sol

# Solution 하면서 내가 놓쳤던 부분
# 1. if 가 아닌 filter 로 사용할 수 있다..
# 2. ' '.join() 을 활용하면 다시 strip 를 안해도 된다..
# 3. [::-1] 을 활용해서 바로 거꾸로 넣을 수 있다..

# 투 포인터를 사용한 해결 방법(이론)
# 문자열 전체에 대한 투포인터로 풀 수 있음!
# + Stack 을 활용해서 꺼꾸로 가지고 오면 됨.

# solution
def solution(s):
    s = s.strip()
    return ' '.join(list(filter(len, s.split(' ')))[::-1])


if __name__ == '__main__':
    s = "  the sky   is    blue"
    sol = solution(s)
    print(sol)
def solution(s, k):
    def small_answer(s):
        result = float('inf')
        for i in range(len(s)):
            pic = int(s[:i] + s[i+1:])
            if pic < result:
                result = pic
        return str(result)
    answer = s
    for _ in range(k):
        answer = small_answer(answer)
    return answer

# solution
# greedy 로 구현하는 방식.
# 앞에 두번째 수가 0이 오지 않는 한 제일 큰 값을 없애는게 좋기 때문에 그렇게 구현
# 모든 수를 비교하지 않고 최적화 가능
def solution(s, k):
    if k >= len(s): # 실제로 발생할 수 있는 조건 고려
        return "0"
    
    if k == 0:
        return s.lstrip('0')
    
    if s[1] == '0':
        return solution(s[1:].lstrip('0'),k-1) # 한번에 두개가 없어지는 경우에, k 가 s 보다 적을 수 있기 때문에 위 조건 필요
    else:
        ind = 0
        for i in range(1, len(s)):
            if s[i-1] <= s[i]:
                ind = i
            else:
                break
        return solution(s[:ind] + s[ind+1:], k-1)

if __name__ == '__main__':
    s = "105990"
    k = 1
    sol = solution(s, k)
    print(sol)
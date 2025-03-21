# Problem2

## 문제 설명
# 회문 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 같은 순서의 문자로 구성된 문자열을 말한다.  
# - 예시) `'abba'`, `'kayak'`, `'madam'`

# 유사회문은 문자열 그 자체는 회문이 아니지만 한 문자를 삭제하면 회문이 되는 문자열을 말한다.  
# - 예시) `'summuus'`의 5번째 또는 6번째 문자 `'u'`를 제거하면 `'summus'`인 회문을 만들 수 있다.

# 주어진 문자열을 확인한 후 문자열 종류에 따라 다음과 같이 출력하는 프로그램을 작성하세요.

# - 회문: 0
# - 유사회문: 1
# - 기타: 2

## 입력 예시

# |입력|출력|
# |---|---|
# |`'abba'`|`0`|
# |`'summuus'`|`1`|
# |`'xabba'`|`1`|
# |`'xabbay'`|`2`|
# |`'comcom'`|`2`|
# |`'comwwmoc'`|`0`|
# |`'comwwtmoc'`|`1`|

def solution(s):
    for i in range(len(s)//2):
        end = i+1
        if s[i] != s[-end]:
            if s[i] == s[-end-1]:
                check = solution(s[i:-end-1])
                return 1 if check == 0 else check
            elif s[i+1] == s[-end]:
                check = solution(s[i+1:-end+1])
                return 1 if check == 0 else check
            else:
                return 2
        if s[i] == s[-i]:
            continue
    return 0

# 모범 답안
def solution(s):
    def solve(l, r, k):
        if l >= r: # 탈출 조건
            return 0
        
        if s[l] == s[r]: # 두개의 문자 비교
            return solve(l+1, r-1, k)
        
        elif k > 0: # 하나도 지우지 않은 경우
            if solve(l+1,r,k-1) == 0 or solve(l, r-1, k-1) == 0: # 지웠을 경우 회문인지 확인
                return 1
        return 2
    
    return solve(0,len(s)-1, 1)
    


if __name__ == '__main__':
    s = 'suummus'
    sol = solution(s)
    print(sol)
    print(solution('abba'))
    print(solution('summuus'))
    print(solution('xabba'))
    print(solution('xabbay'))
    print(solution('comcom'))
    print(solution('comwwmoc'))
    print(solution('comwwtmoc'))
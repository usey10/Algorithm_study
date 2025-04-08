def solution(num):
    a = list(str(num))
    result = num
    N = len(a)
    for i in range(N-1):
        for j in range(i+1, N):
            a[i], a[j] = a[j], a[i]
            a_int = ""
            if int(a_int.join(a)) > result:
                result = int(a_int.join(a))
    return result

# 2번 문제 풀고 다시 작성
# 이랬을떄 문제점 : a[0] 이 max 였는데, 다른 자리 수를 바꿀 경우도 있다.
def solution(num):
    a = list(str(num))
    if a[0] == max(a):
        return num
    else:
        ind = 0
        for i in range(len(a)):
            if a[ind] < a[i]:
                ind = i
            else:
                continue
        a[0], a[ind] = a[ind], a[0]
        return "".join(a)
    
# solution
def solution(num):
    digits = list(map(int, list(str(num))))

    inc_ind = -1
    for i in range(1, len(digits)):
        if digits[i] > digits[i-1]:
            inc_ind = i
            break

    # 교환하지 않는 경우 : 앞 숫자가 뒤 숫자보다 무조건 큰 경우
    if inc_ind == -1:
        return -1
    
    max_val = digits[inc_ind]
    max_ind = inc_ind
    # 감소하지 않은 index 부터 제일 인덱스가 크고, 크기가 큰 수 찾기
    for i in range(inc_ind+1, len(digits)):
        if digits[i] >= max_val:
            max_val = digits[i]
            max_ind = i
    # 변경할 앞 인덱스 찾기
    for i in range(inc_ind):
        if digits[i] < max_val:
            digits[max_ind], digits[i] = digits[i], digits[max_ind]
            return int(''.join(map(str, digits)))

if __name__ == '__main__':
    num = 43824
    sol = solution(num)
    print(sol)

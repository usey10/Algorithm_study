# 못풀음.

# tabularization
# 도달 가능 여부 + 도달 최대 위치를 확인하기
# solution

def solution(nums):
    N = len(nums)
    max_reach = 0

    for i in range(N):
        if max_reach >= i:
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= N-1:
                return True
    return True


if __name__ == '__main__':
    nums = [3, 4, 1, 1, 0, 3]
    sol = solution(nums)
    print(sol)

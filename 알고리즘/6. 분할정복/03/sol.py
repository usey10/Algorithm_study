def solution(nums):
    def list_sum(list, n):
        max_num = 0
        for i in range(len(list)-n-1):
            if max_num < sum(list[i:i+n+1]):
                max_num = sum(list[i:i+n+1])
        return max_num
    result = sum(nums)

    for j in range(len(nums)+1):
        j_num = list_sum(nums, j+1)
        if result < j_num:
            result = j_num
    return result

# solution
# 위 문제점 : 최적화가 안됨. + 제대로 구현 못함.. -> for 및 재귀로 시간 복잡도가 놓음.
# 반을 나누면 재귀적으로 풀 수 있지만 반 걸친 경우에 대한 내용의 확인이 어려움
# -> 투포인터로 확인(중간 두 값을 i, j 로 놓고 앞으로, 뒤로 가면서 더해서 가장 큰 값을 찾기
def solution(nums):
    def solve(left, right):
        if left == right:
            return nums[left]
        
        mid = (left + right) // 2
        sol_left = solve(left, mid)
        sol_right = solve(mid + 1, right)
        sol_mid = solve_mid(left, mid, right)
        return max(sol_left, sol_right, sol_mid)
    
    def solve_mid(left, mid, right):
        max_left = -float('inf')
        curr_sum = 0
        for i in range(mid, left-1, -1):
            curr_sum += nums[i]
            max_left = max(max_left, curr_sum)

        max_right = -float('inf')
        curr_sum = 0
        for i in range(mid + 1, right + 1):
            curr_sum += nums[i]
            max_right = max(max_right, curr_sum)
        
        return max_left + max_right

    return solve(0, len(nums)-1)

if __name__ == '__main__':
    nums = [-5, 0, -3, 4, -1, 3, 1, -5, 8]
    sol = solution(nums)
    print(sol)

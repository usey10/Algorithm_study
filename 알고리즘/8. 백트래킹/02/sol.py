# solution
# 7 체크 -> 71 체크 -> 719 체크 -> 7193 체크

from math import factorial

def is_prime(x):
    # wilson's theorem
    if x < 2:
        return False
    return factorial(x-1) % x == x - 1

def solution(n):
    result = []
    
    def dfs(nums):
        def is_promising(nums, k):
            return is_prime(int(''.join(map(str, nums + [k]))))
        
        if len(nums) == n:
            result.append(int(''.join(map(str, nums))))
            return
        
        for i in range(10):
            if is_promising(nums, i):
                nums += [i]
                dfs(nums)
                del nums[-1]
    
    dfs([])
    return result


if __name__ == '__main__':
    N = 2
    sol = solution(N)
    print(sol)

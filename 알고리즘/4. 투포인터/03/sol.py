def solution(arr, target):
    result = 0
    for i in range(len(arr)-2):
        left = i
        right = i + 3
        sum_a = sum(arr[left:right])
        if abs(target-result) > abs(target-sum_a):
            result = sum_a
        elif abs(target-result) == abs(target-sum_a):
            result = min(result, sum_a)
    return result

# solution
# arr 오름차순으로 정렬 -> 3개의 값 선택(left, mid, right)
# left 고정 후 mid, right 변경
# 값이 작음 -> 값을 키움(mid 증가)
# 값이 큼 -> 값을 작게 만듬(right 감소) -> left 를 고정했을떄 나머지 다 해보고 left 변경

def solution(arr, target):
    N = len(arr)
    closest_diff = float('inf')
    closest_sum = 0
    arr.sort()

    for left in range(N-2):
        mid = left + 1
        right = N - 1

        while mid < right:
            curr_sum = arr[left] + arr[mid] + arr[right]
            curr_diff = abs(target - curr_sum)
            
            if curr_diff < closest_diff:
                closest_diff = curr_diff
                closest_sum = curr_sum
            elif curr_diff == closest_diff and closest_sum > curr_sum:
                closest_sum = curr_sum
            
            if curr_sum < target:
                mid += 1
            elif curr_sum > target:
                right -= 1
            else:
                return target
            
    return closest_sum


    pass

if __name__ == '__main__':
    arr = [5, 2, 15, 3, 10, 12]
    target = 21
    sol = solution(arr, target)
    print(sol)

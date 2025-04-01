# 반복문
def solution1(arr, target):
    index = len(arr)//2
    for _ in range(len(arr)):
        if arr[index] == target:
            return index
        elif target < arr[index]:
            if target > arr[index-1]:
                return -1
            index = index // 2
        elif target > arr[index]:
            if target < arr[index+1]:
                return -1
            index += index // 2 + 1

# solution
def solution1(arr, target):
    left = 0
    right = len(arr) - 1

    mid = (left+right) // 2
    while left <= right:
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1

# 재귀호출 / Solution
def solution2(arr, target, left=0, right=None):
    if right is None: # 초기화 작업
        right = len(arr) - 1

    if left > right:
        return -1 # 탈출 조건
    
    mid = (left+right) // 2
    if arr[mid] == target:
        return mid

    if arr[mid] > target:
        return solution2(arr, target, left, mid-1)
    else:
        return solution2(arr, target, mid+1, right)

# 반복문이라고 해서 무조건 For 문으로 할 필요 없음..
# While 쓰는것도 계속 생각해볼것.
# 필요한 변수 지정 하기!
# 재귀 계속 연습 필요.


if __name__ == '__main__':
    arr = [10, 20, 40, 50, 60, 70]
    target = 40

    sol = solution1(arr, target)
    print(sol)

    sol = solution2(arr, target)
    print(sol)

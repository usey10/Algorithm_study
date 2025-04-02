def solution(weights, delivery):
    total = 0
    for i in weights:
        total += i
    
    day = total // delivery
    print(day)
    day_list = 0
    result = 0
    for i in weights:
        while day_list > day:
            if result < day_list:
                result = day_list - i
            print(i)
            day_list = 0
        day_list += i
    return result

# 접근법 : 전체 값에 대한 Delivery 에 집중함.
# -> 그 이후에 비교 하는 부분에서 구현 실패

# solution
# 실패, 성공여부에 대한 이진 탐색!
# 찾고자 하는 반환 값 : 차량 적재량 0~전체 중에서 성공하는 최소값.
def solution(weights, delivery):
    left = max(weights)
    right = sum(weights)
    answer = float('inf')

    while left < right:
        mid = (left + right) // 2

        days = 1
        current_weight = 0

        for w in weights:
            if current_weight + w > mid:
                days += 1
                current_weight = 0
            current_weight += w

        if days > delivery:
            left = mid + 1
        else:
            answer = min(answer, mid)
            right = mid - 1
        
    return answer


if __name__ == '__main__':
    weights = [3, 2, 2, 4, 1, 4]
    delivery = 3
    sol = solution(weights, delivery)
    print(sol)
    
def solution(activity):
    start, end = 0, 0
    result = 0
    pic = sorted(activity, key=lambda x:x[1])
    for i, j in pic:
        if end < i and start < i:
            start, end = i, j
            result += 1
        elif end > i:
            continue
    return result

# solution
# 참고 사항 : start 를 주지 않아도 됐을 듯.
def solution(activity):
    items = [(x[1], x[0]) for x in activity]
    items.sort()

    count = 0
    last_end_time = 0
    for event in items:
        end_time, start_time = event
        if start_time < last_end_time:
            continue
        else:
            count += 1
            last_end_time = end_time
    return count


if __name__ == '__main__':
    activity = [[1, 5], [4, 6], [3, 5], [7, 12], [5, 11], [13, 15]]
    sol = solution(activity)
    print(sol)

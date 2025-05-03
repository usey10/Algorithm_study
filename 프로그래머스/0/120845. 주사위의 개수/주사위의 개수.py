def solution(box, n):
    answer = 1
    for box_len in box:
        answer *= box_len // n

    return answer
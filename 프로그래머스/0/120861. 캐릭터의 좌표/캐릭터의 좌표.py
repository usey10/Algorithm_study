def solution(keyinput, board):
    answer = [0,0]
    b_range = [i // 2 for i in board]
    for i in keyinput:
        change = 1 if i == "up" or i == "right" else -1
        if i == "up" or i == "down":
            if abs(answer[1] + change) <= b_range[1]:
                answer[1] += change
        else:
            if abs(answer[0] + change) <= b_range[0]:
                answer[0] += change
    return answer
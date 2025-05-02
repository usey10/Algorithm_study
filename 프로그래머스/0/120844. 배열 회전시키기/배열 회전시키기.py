def solution(numbers, direction):
    if direction == 'left':
        numbers.append(numbers[0])
        return numbers[1:]
    else:
        answer = []
        answer.append(numbers[-1])
        answer.extend(numbers[:-1])
        return answer
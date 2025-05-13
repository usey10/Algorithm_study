def solution(numbers):
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    
    numbers_up = [i for i in numbers if i > 0]
    numbers_down = [i for i in numbers if i < 0]
    
    if len(numbers_up) == 1 and len(numbers_down) and 0 in numbers:
        return 0
    
    if len(numbers_up) >= 2 & len(numbers_down) >= 2:
        up_max = sorted(numbers_up)[-1] * sorted(numbers_up)[-2]
        down_max = sorted(numbers_down)[-1] * sorted(numbers_down)[-2]
        return max(up_max, down_max)
    elif len(numbers_up) >= 2 & len(numbers_down) < 2:
        return sorted(numbers_up)[-1] * sorted(numbers_up)[-2]
    else:
        return sorted(numbers_down)[-1] * sorted(numbers_down)[-2] 
    
    return answer
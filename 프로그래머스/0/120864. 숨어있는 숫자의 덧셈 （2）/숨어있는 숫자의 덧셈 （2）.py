def solution(my_string):
    numbers = []
    
    for i in range(len(my_string)):
        if my_string[i].isdigit():
            if my_string[i-1].isdigit() and i != 0:
                before_num = numbers.pop(-1)
                before_num = before_num + my_string[i]
                numbers.append(before_num)
            else:
                numbers.append(my_string[i])
    
    return sum(map(int, numbers))
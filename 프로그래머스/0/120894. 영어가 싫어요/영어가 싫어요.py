def solution(numbers):
    number_set = ['zero','one','two','three','four','five','six','seven','eight','nine']
    number_check = ''
    answer = []
    for i in numbers:
        number_check += i
        if number_check in number_set:
            answer.append(number_set.index(number_check))
            number_check = ''

    return int(''.join(str(i) for i in answer))
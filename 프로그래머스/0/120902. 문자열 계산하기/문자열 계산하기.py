def solution(my_string):
    string_list = my_string.split(" ")
    answer = int(string_list[0])
    for i in range(1, len(string_list)):
        if string_list[i] == '+':
            answer += int(string_list[i+1])
        elif string_list[i] == '-':
            answer -= int(string_list[i+1])
        else:
            pass
    return answer
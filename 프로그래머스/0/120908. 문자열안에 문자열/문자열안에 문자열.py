def solution(str1, str2):
    answer = []
    for i in range(len(str1)-len(str2)+1):
        answer.append(str1[i:i+len(str2)])

    return 1 if str2 in answer else 2
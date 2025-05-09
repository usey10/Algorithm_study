def solution(quiz):
    answer = []
    for i in quiz:
        result = 0
        check = i.split(" ")
        ans = int(check[-1])
        res = int(check[0])+int(check[2]) if check[1] == "+" else int(check[0])-int(check[2])
        
        if ans == res:
            answer.append("O")
        else:
            answer.append("X")

    return answer
def solution(polynomial):
    pol_list = polynomial.split(" ")
    
    while "+" in pol_list:
        pol_list.remove("+")
        
    x = 0
    y = 0
    
    for i in pol_list:
        if i.isdigit():
            y += int(i)
        else:
            x += (int(i[:-1]) if i[:-1].isdigit() else 1)
    answer = []
    
    if x > 1:
        answer.extend([f"{x}","x"])
        if y > 0:
            answer.append(f" + {y}")
        print(answer)
    elif x > 0:
        answer.append("x")
        if y > 0:
            answer.append(f" + {y}")
    else:
        return str(y)
    
    return "".join(answer)

def solution(babbling):
    speak = ["aya", "ye", "woo", "ma"]
    for i in range(len(babbling)):
        for j in speak:
            babbling[i] = babbling[i].replace(j, " ")
        babbling[i] = babbling[i].replace(" ", "")
        
    print(babbling)
    return babbling.count("")
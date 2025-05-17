def solution(score):
    answer = [sum(i)/2 for i in score]
    result = []
    for i in answer:
        rank_i = len(list(filter(lambda x:x>i, answer))) + 1
        result.append(rank_i)
        
    return result
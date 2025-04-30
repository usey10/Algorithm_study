def solution(emergency):
    rank_em = {j:i+1 for i,j in enumerate(sorted(emergency, reverse = True))}
    return [rank_em[i] for i in emergency]
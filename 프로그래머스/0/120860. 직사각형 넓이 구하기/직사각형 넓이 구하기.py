def solution(dots):
    N = len(dots)
    x = max(dots[i][0] for i in range(N)) - min(dots[i][0] for i in range(N))
    y = max(dots[i][1] for i in range(N)) - min(dots[i][1] for i in range(N))
    return x*y
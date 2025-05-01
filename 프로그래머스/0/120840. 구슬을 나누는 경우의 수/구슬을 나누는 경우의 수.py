def solution(balls, share):
    def all_method(n, t):
        result = 1
        if t == 1:
            for i in range(t, n+1):
                result *= i
        else:
            for i in range(n-t+1, n+1):
                result *= i
        return result
    return all_method(balls, share) / all_method(share, 1)
def solution(M, N):
    if M == 1 and N == 1:
        return 0
    elif M == 1:
        return N - 1
    elif N == 1:
        return M -1
    else:
        return M*N - 1
 
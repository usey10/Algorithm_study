def solution(A, B):
    a_set = [A[j:] + A[0:j] for j in range(len(A),0,-1)]
    print(B in a_set)
    if B in a_set:
        return a_set.index(B)
    else:
        return -1

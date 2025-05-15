def solution(a, b):
    b_m = [i for i in range(1, b+1) if b % i == 0]
    b_m.remove(1)

    for i in b_m:
        if i % 2 and i % 5:
            if a % i:
                return 2
            continue
        else:
            continue

    return 1
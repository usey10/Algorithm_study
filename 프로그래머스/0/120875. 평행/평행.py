def solution(dots):
    def absto(x, y):
        return (x[1]-y[1])/(x[0]-y[0])
     
    check1 = absto(dots[0], dots[1]) == absto(dots[2], dots[3])
    check2 = absto(dots[0], dots[2]) == absto(dots[1], dots[3])
    check3 = absto(dots[0], dots[3]) == absto(dots[1], dots[2])

    return 1 if check1+check2+check3 else 0
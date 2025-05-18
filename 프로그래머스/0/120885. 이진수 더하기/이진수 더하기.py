def solution(bin1, bin2):
    cal1 = bin1[::-1]
    cal2 = bin2[::-1]
    
    N = len(bin1)
    M = len(bin2)
    cal_r = ""
    for i in range(min(N,M)):
        cal_r += str(int(cal1[i]) + int(cal2[i]))
        
    print(cal_r)
    if M - N:
        cal_r += str(cal2[N:M])
    if N - M:
        cal_r += str(cal1[M:N])
    print(cal_r)
    before = 0
    result = ""
    for j in cal_r:
        c_n = int(j) + before
        if c_n == 2:
            before = 1
            result += "0"
        elif c_n == 3:
            before = 1
            result += "1"
        else:
            result += str(c_n)
            before = 0
    print(result, before)
    if before >= 1:
        result += str(before)

    return result[::-1]
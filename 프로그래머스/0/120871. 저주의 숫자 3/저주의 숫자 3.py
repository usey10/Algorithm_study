def solution(n):
    def check(k):
        if k == 1 or k == 2:
            return k
        if k > 200:
            return -1
        
        if "3" not in str(k) and k % 3 != 0:
            return k
        else:
            return check(k+1)
        
        
    def num3(k):
        if k == 1 or k == 2:
            return k
        return check(num3(k-1) + 1)
    
    return num3(n)

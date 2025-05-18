# 1999
# 1999장 발급 서비스 치킨 199 마리 쿠폰 9개
# 199장 발급 서비스치킨 19 마리 쿠폰 9개
# 19 장 발급 서비스 치킨 1마리 쿠폰 9개
# 1장 발급 
# 28장 발급 서비스 치킨 2마리 쿠폰 7개
# 199 + 19 + 1 + 2 = 

def solution(chicken):
    coupon = 0
    left = chicken % 10
    service = chicken // 10
    
    while service:
        coupon += service
        left += service % 10
        service = service // 10
    while left // 10:
        coupon += left // 10
        left = left // 10 + left % 10
        
    return coupon
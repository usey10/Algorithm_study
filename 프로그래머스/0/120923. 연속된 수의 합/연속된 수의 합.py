def solution(num, total):
    mid = total // num
    if num % 2 == 1:
        answer = [i for i in range(mid-(num//2), mid+(num//2)+1)]
    else:
        answer = [i for i in range(mid-(num//2)+1, mid+(num//2)+1)]
    return answer
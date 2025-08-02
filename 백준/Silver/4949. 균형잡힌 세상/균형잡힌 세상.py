import sys
from collections import deque


while True:
    sentence = sys.stdin.readline().rstrip()
    str_deque = deque()

    if sentence == ".":
        break
    
    result = "yes"
    for s in sentence:
        if s in ["[", "("]:
            str_deque.append(s)
        elif s == ")":
            if len(str_deque) == 0:
                result = "no"
                break
            last_str = str_deque.pop()
            if last_str != "(":
                result = "no"
                break
        elif s == "]":
            if len(str_deque) == 0:
                result = "no"
                break

            last_str = str_deque.pop()
            if last_str != "[":
                result = "no"
                break
        elif s == ".":
            break
        else:
            continue

    if len(str_deque):
        print("no")
    else:
        print(result)
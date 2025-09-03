import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
M = int(input().rstrip())

p = "I" + ("OI" * N)
S = input().rstrip()


idx = 0
cnt = 0

while idx < M-(N*2):
    if S[idx] == "O":
        idx += 1
        continue
    else:
        i = idx + 1
        if S[i] == "O":
            new_word = S[idx:idx+len(p)]
            # print(new_word)

            if new_word == p:
                cnt += 1
            
            idx += 2
        else:
            idx += 1
            continue


print(cnt)


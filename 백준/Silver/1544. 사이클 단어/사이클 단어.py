import sys

N = int(sys.stdin.readline())

all_words = set()
count = 0

for _ in range(N):
    x = sys.stdin.readline().rstrip()
    if x in all_words:
        continue
    else:
        for i in range(len(x)):
            word = x[i:]+x[0:i]
            all_words.add(word)
        count += 1
    
print(count)
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
data = input().strip()

visited = [False] * (len(data))
count = 0

for i in range(len(data)):
    if data[i] == 'P':
    
        start = i-K if i-K >= 0 else 0
        end = i+K+1 if i+K+1 < N else N
        for j in range(start, end):
            if data[j] == 'H' and not visited[j]:
                visited[j] = True
                count += 1
                break

print(count)


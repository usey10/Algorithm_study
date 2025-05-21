N = int(input())

for _ in range(N):
    input_str = input()
    stack = []
    answer = "YES"
    for i in input_str:
        if i == "(":
            stack.append(i)
        else:
            if stack:
                stack.pop()
            else:
                answer = "NO"
                continue
    if stack:
        answer = "NO"
    print(answer)
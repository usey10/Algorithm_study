import sys

temp_num = 0

while True:
    temp = sys.stdin.readline().rstrip()
    temp_num += 1
    if "-" in temp:
        break

    stack = []
    count = 0
    for i in temp:
        if i == "{":
            stack.append(i)
        else:
            if stack:
                x = stack.pop()
            else:
                count += 1
                stack.append("{")
    
    count += len(stack) // 2

    print(f"{temp_num}. {count}")
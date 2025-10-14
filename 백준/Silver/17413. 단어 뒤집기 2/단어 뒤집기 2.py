import sys

input = sys.stdin.readline

S = input().rstrip()

stack = []
tag_w = ""
tag = False
sw = [" ", "<", ">"]

result = ""

for i in S:
    if i not in sw and not tag:
        # 문자열이고, 태그가 아닐때
        stack.append(i)
    elif i == " " and not tag:
        # 태그가 아니고, 공백일떄
        while stack:
            result += stack.pop()
        result += " "
    elif i == "<":
        while stack:
            result += stack.pop()
        
        tag = True

    elif i == ">":
        result += "<" + tag_w + ">"

        tag_w = ""
        tag = False
    else:
        tag_w += i

while stack:
    result += stack.pop()

if result[0] == " ":
    result = result.lstrip()
if result[-1] == " ":
    result = result.rstrip()


print(result)


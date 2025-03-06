# python 에서 스택 사용하기(리스트 응용)

stack = []

# push 동작
for i in range(1,10):
    stack.append(i)

print(stack)

# peek 동작
print(stack[-1]) # -1 인덱스로 구현

# pop 동작
for i in range(1,10):
    val = stack.pop()
    print(val, end=" ")

print()

# is_empty 동작
print(len(stack) == 0) # 스택의 길이로 판단
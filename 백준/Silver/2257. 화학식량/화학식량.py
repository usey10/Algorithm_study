import sys

chems = {"H":1, "C":12, "O":16}
chem = sys.stdin.readline().rstrip()
stacks = []

for i in chem:
    if i == "(":
        stacks.append(i)
    elif i == ")":
        stack_ca = 0
        while stacks[-1] != "(":
            x = stacks.pop()
            stack_ca += x
        stacks.pop()
        stacks.append(stack_ca)
    elif i.isnumeric():
        x = stacks.pop()
        x = x * int(i)
        stacks.append(x)
    else:
        stacks.append(chems[i])


print(sum(stacks))
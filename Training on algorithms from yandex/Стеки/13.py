st = input().strip().split()
stack = list()
flag = False
for elem in st:
    if elem in "-+*":
        if len(stack) >= 2:
            first, second = stack[-2], stack[-1]
            del stack[-1]
            del stack[-1]
            if elem == "+":
                stack.append(first + second)
            elif elem == "-":
                stack.append(first - second)
            else:
                stack.append(first * second)
        elif len(stack) == 1:
            stack[0] = stack[0] * (-1)
        else:
            flag = True
    else:
        if flag:
            stack.append(int(elem) * (-1))
        else:
            stack.append(int(elem))
print(stack[0])
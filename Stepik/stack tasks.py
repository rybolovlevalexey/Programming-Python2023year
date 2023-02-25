stack = list()
flag = True
for elem in input():
    if elem in "({[":
        stack.append(elem)
    else:
        if len(stack) == 0:
            flag = False
            break
        lst = stack.pop(-1)
        if not ((elem == ")" and lst == "(") or (elem == "}" and lst == "{") or \
                (elem == "]" and lst == "[")):
            flag = False
            break
if flag and len(stack) == 0:
    print("YES")
else:
    print("NO")
def main(st):
    stack = list()
    for elem in st:
        if elem in "{[(":
            stack.append(elem)
        else:
            if len(stack) == 0:
                return False
            if (elem == ")" and stack[-1] != "(") or (elem == "}" and stack[-1] != "{") or \
                    (elem == "]" and stack[-1] != "["):
                return False
            del stack[-1]
    if len(stack) == 0:
        return True
    return False


line = input()
if main(line):
    print("yes")
else:
    print("no")
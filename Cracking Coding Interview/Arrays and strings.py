st = input()  # original string
letters = ""
flag = True
for elem in st:
    if elem in letters:
        flag = False
        break
    else:
        letters += elem
if flag:
    print("All letters in string do not repeat")
else:
    print("There is letter, which repeat")

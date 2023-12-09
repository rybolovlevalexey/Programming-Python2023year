words_dict = dict()
for value in input().split():
    words_dict[len(value)] = words_dict.get(len(value), list()) + [value]
text = input().split()
ans = list()
for elem in text:
    flag = False
    for key in sorted(filter(lambda x: x < len(elem), words_dict.keys())):
        for word in words_dict[key]:
            if elem.startswith(word):
                ans.append(word)
                flag = True
                break
        if flag:
            break
    if not flag:
        ans.append(elem)

print(" ".join(ans))
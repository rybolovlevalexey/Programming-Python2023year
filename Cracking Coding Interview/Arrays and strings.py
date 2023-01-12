st1 = input()
st2 = input()
if abs(len(st2) - len(st1)) >= 2 or st1 == st2:
    print("NO")
else:
    letters = dict()
    if len(st1) == len(st2):
        for i in range(len(st1)):
            if st1[i] in letters:
                letters[st1[i]] += 1
            else:
                letters[st1[i]] = 1
            if st2[i] in letters:
                letters[st2[i]] -= 1
            else:
                letters[st2[i]] = -1
        res = len(list(filter(lambda x: x != 0, letters.values())))
        if res == 2:
            first = ""
            second = ""
            for key, value in letters.items():
                if value == 1:
                    first = key
                if value == -1:
                    second = key
            print(first, second)
            sp = st1.count(first) * [st1]
            print(sp)
            for i in range(len(sp)):
                sp[i] = sp[i].replace(first, second, i + 1)
                sp[i] = sp[i].replace(second, first, i)
            print(sp)
            if st2 in sp:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    else:
        for i in range(len(st1)):
            if st1[i] in letters:
                letters[st1[i]] += 1
            else:
                letters[st1[i]] = 1
        for i in range(len(st2)):
            if st2[i] in letters:
                letters[st2[i]] -= 1
            else:
                letters[st1[i]] = -1
        res = len(list(filter(lambda x: x != 0, letters.values())))
        if res == 1:
            print("YES")
        else:
            print("NO")

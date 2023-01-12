st1 = input()
st2 = input()
if len(st1) != len(st2):
    print("NO")
else:
    letters = dict()
    for i in range(len(st1)):
        if st1[i] in letters:
            letters[st1[i]] += 1
        else:
            letters[st1[i]] = 1

        if st2[i] in letters:
            letters[st2[i]] -= 1
        else:
            letters[st2[i]] = -1
    if len(set(letters.values())) == 1:
        print("YES")
    else:
        print("NO")
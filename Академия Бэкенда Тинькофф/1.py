n = int(input())
answers = dict()
for h in range(1, n + 1):
    if h == 1:
        answers[h] = 1
        print(0, end=" ")
    else:
        s = (2 * h - 1) ** 2
        v = (2 * h - 1) ** 3
        cost = v - (s + answers[h - 1])
        answers[h] = answers[h - 1] + s
        print(cost, end=" ")

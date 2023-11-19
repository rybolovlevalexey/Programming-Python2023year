n, m, q = map(int, input().split())
first: dict[str, int] = dict()
second: dict[str, int] = dict()
for elem1 in input().split():
    if elem1 in first:
        first[elem1] += 1
    else:
        first[elem1] = 1
for elem2 in input().split():
    if elem2 in first and first[elem2] > 0:
        first[elem2] -= 1
    else:
        second[elem2] = second.get(elem2, 0) + 1
result = sum(first.values()) + sum(second.values())

for i in range(q):
    action, player, card = input().split()
    if action == "1":
        if player == "A":
            if card in second and second[card] > 0:
                second[card] -= 1
                result -= 1
            else:
                result += 1
                first[card] = first.get(card, 0) + 1
        elif player == "B":
            if card in first and first[card] > 0:
                first[card] -= 1
                result -= 1
            else:
                result += 1
                second[card] = second.get(card, 0) + 1
    else:
        if player == "A":
            if card in first and first[card] > 0:
                result -= 1
                first[card] -= 1
            else:
                second[card] = second.get(card, 0) + 1
                result += 1
        else:
            if card in second and second[card] > 0:
                result -= 1
                second[card] -= 1
            else:
                result += 1
                first[card] = first.get(card, 0) + 1
    print(result, end=" ")

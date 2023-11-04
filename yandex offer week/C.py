def find_best_person(sp, t):
    result = list()
    for elem in sp:
        if result == list() or result[1] < persons[elem][0] + (t - persons[elem][1]) or \
                (result[1] == persons[elem][0] + (t - persons[elem][1]) and result[0] > elem):
            result = [elem, persons[elem][0] + (t - persons[elem][1])]
    return result


n = int(input())
# имя: (общая опытность, момент начала текущего рабочего цикла или -1, если не работает)
persons: {str: list[int]} = dict()
team = set()
team_length = 0
last_time = None
summa = 0
best_person = list()  # [имя, опытность]

for i in range(n):
    name, time = input().split()
    time = int(time)
    delta = time - last_time if last_time is not None else 0
    if len(best_person) != 0:
        best_person[1] += delta

    # обработка текущего события
    if name not in team:
        summa += team_length * delta
        team_length += 1
        # пришёл в команду
        team.add(name)  # добавление в текущий состав команды
        if name not in persons:  # ни разу не был в команде
            persons[name] = [0, time]
        else:  # когда-то уже был в команде
            persons[name][1] = time
            summa += persons[name][0]

        if best_person == list() or best_person[1] < persons[name][0] or \
                (best_person[1] == persons[name][0] and best_person[0] > name):
            best_person = [name, persons[name][0]]
    else:
        summa += team_length * delta
        team_length -= 1
        team.remove(name)
        if name == best_person[0]:
            best_person = find_best_person(team, time)
        persons[name][0] += time - persons[name][1]
        persons[name][1] = -1
        summa -= persons[name][0]

    print(best_person[0], summa - best_person[1] * 2)
    last_time = time

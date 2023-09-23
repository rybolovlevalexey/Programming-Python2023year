n, k = map(int, input().split())  # кол-во абитуриентов, программ
programs = dict()  # номер программы: кол-во мест
st = input().split()
for i in range(k):
    programs[i + 1] = int(st[i])
students = dict()  # порядковый номер(с нуля): [рейтинг, [приоритеты]]
answer = [0] * n
for i in range(n):
    r, colvo, *prior = map(int, input().split())
    students[i] = [r, prior]

for key in sorted(students.keys(), key=lambda x: students[x][0]):
    for pr in students[key][1]:  # перебор приоритетов поступающего
        if programs[pr] > 0:
            answer[key] = pr
            programs[pr] -= 1
            break
    else:
        answer[key] = -1
print(*answer)
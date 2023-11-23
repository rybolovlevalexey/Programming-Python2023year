DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date1 = list(map(int, input().split()))
date2 = list(map(int, input().split()))

if date2[1] == date1[1] and date2[2] != date2[2]:
    raise ZeroDivisionError

date1[1] -= 1
date2[1] -= 1
result = [0, 0]
if date1[-3] > date2[-3] or (date1[-3] == date2[-3] and date1[-2] > date2[-2]) or \
        (date1[-3] == date2[-3] and date1[-2] == date2[-2] and date1[-1] > date2[-1]):
    result[0] -= 1

if date2[-1] < date1[-1]:
    if date2[-2] == 0:
        date2[-3] -= 1
        date2[-2] += 60
    date2[-2] -= 1
    date2[-1] += 60
result[1] += date2[-1] - date1[-1]

if date2[-2] < date1[-2]:
    date2[-2] += 60
    date2[-3] -= 1
result[1] += (date2[-2] - date1[-2]) * 60

if date2[-3] < date1[-3]:
    date2[-3] += 24
result[1] += (date2[-3] - date1[-3]) * 60 * 60

result[0] += (date2[0] - date1[0]) * 365
if date2[1] > date1[1]:
    result[0] += sum(DAYS_IN_MONTH[date1[1] + 1: date2[1]])
    result[0] += date2[2] + (DAYS_IN_MONTH[date1[1]] - date1[2])
elif date2[1] == date1[1]:
    if date2[2] == date2[2]:
        pass
    elif date2[2] > date1[2]:
        result[0] += date2[2] - date1[2]
    else:
        result[0] += sum(DAYS_IN_MONTH) - abs(date2[2] - date1[2])
else:
    result[0] += sum(DAYS_IN_MONTH[date1[1] + 1:]) + sum(DAYS_IN_MONTH[:date2[1]])
    result[0] += (DAYS_IN_MONTH[date1[1]] - date1[2]) + date2[2]
print(*result)
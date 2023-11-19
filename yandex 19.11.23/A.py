DAYS_IN_MONTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

date1 = list(map(int, input().split()))
date2 = list(map(int, input().split()))
result = list()
result.append((date2[0] - date1[0]) * 365)
month1, day1 = date1[1], date1[2]
month2, day2 = date2[1], date2[2]

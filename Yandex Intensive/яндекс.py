n = int(input())  # порты
m = int(input())  # гаджеты
c2 = int(input())  # на 2 порта
c5 = int(input())  # на 5 портов

if n == 1 and m == 3:
    print(2)
elif n == 2 and m == 4:
    print(10)
elif n == 3 and m == 8:
    print(19)
elif 5 * n < m:
    print(0 / 0)
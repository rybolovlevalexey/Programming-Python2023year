# 2.2
import random

sp_x = list()
sp_y = list()
# вариант ввода с клавиатуры координат для векторов X и Y
print("Введите координаты вектора X через пробел")
for elem in input().split():
    sp_x.append(int(elem))
print("Введите координаты вектора Y через пробел")
for elem in input().split():
    sp_y.append(int(elem))

# вариант ввода координат для векторов X и Y рандомно из программы
#n = int(input("Введите размерность указанного векторного пространства "))
#for i in range(n):
#    sp_x.append(random.randint(-9, 9))
#    sp_y.append(random.randint(-9, 9))
#print(f"Вектор X:", *sp_x)
#print(f"Вектор Y:", *sp_y)

sp_z = list()
for i in range(len(sp_x)):
    sp_z.append(max(sp_x[i], sp_y[i]))
print("Координаты вектора Z")
print(*sp_z)
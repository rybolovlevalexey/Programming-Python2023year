n = int(input())
k = int(input())
ryad = int(input())
place = int(input())
if k == n:
    print(-1)
else:
    flag = True
    first_var = ((ryad - 1) * 2 + place)
    if first_var >= k:
        first_var = first_var % k
    var1 = ((ryad - 1) * 2 + place) - k
    var2 = ((ryad - 1) * 2 + place) + k
    if var1 % 2 == 0:
        ryad1 = var1 // 2
        place1 = 2
    else:
        place1 = 1
        ryad1 = var1 // 2 + 1
    if var2 % 2 == 0:
        ryad2 = var2 // 2
        place2 = 2
    else:
        place2 = 1
        ryad2 = var2 // 2 + 1
    if var1 <= 0:
        if var2 > n:
            flag = False
        else:
            print(ryad2, place2)
    else:
        if var2 > n:
            print(ryad1, place1)
        else:
            d1 = abs(ryad - ryad1)
            d2 = abs(ryad2 - ryad)
            #print(d1, d2, ryad, ryad1, ryad2, var1, var2)
            if d1 == d2 or d2 < d1:
                print(ryad2, place2)
            else:
                print(ryad1, place1)
    if not flag:
        print(-1)

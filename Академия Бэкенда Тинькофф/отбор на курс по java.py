pins = set()
for i1 in range(10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                st = str(i1) + str(i2) + str(i3) + str(i4)
                if len(set(st)) == 4:
                    pins.add(st)
print(len(pins))
print(pins)
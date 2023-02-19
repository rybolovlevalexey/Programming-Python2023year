class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __lt__(self, other):
        return self.x < other.x or self.y < other.y

    def __eq__(self, other):
        return self.x == other.x or self.y == other.y


k = int(input())
x1, y1, x2, y2 = None, None, None, None
for i in range(k):
    xi, yi = map(int, input().split())
    if i == 0:
        x1, y1 = xi, yi
    elif i == 1:
        if Point(x1, y1) == Point(xi, yi) or Point(x1, y1) < Point(xi, yi):
            x2, y2 = xi, yi
        else:
            x2, y2 = x1, y1
            x1, y1 = xi, yi
    else:
        if Point(xi, yi) < Point(x1, y1):
            if xi < x1:
                x1 = xi
            if yi < y1:
                y1 = yi
        if Point(xi, yi) > Point(x2, y2):
            if xi > x2:
                x2 = xi
            if yi > y2:
                y2 = yi

if x2 is None and y2 is None:
    print(x1, y1, x1, y1)
else:
    print(x1, y1, x2, y2)

class Deque:
    def __init__(self):
        self.sp = list()

    def push_front(self, elem):
        self.sp = [elem] + self.sp
        print("ok")

    def push_back(self, elem):
        self.sp.append(elem)
        print("ok")

    def pop_front(self):
        if len(self.sp) == 0:
            print("error")
        else:
            value = self.sp.pop(0)
            print(value)

    def pop_back(self):
        if len(self.sp) == 0:
            print("error")
        else:
            value = self.sp.pop(-1)
            print(value)

    def front(self):
        if len(self.sp) == 0:
            print("error")
        else:
            print(self.sp[0])

    def back(self):
        if len(self.sp) == 0:
            print("error")
        else:
            print(self.sp[-1])

    def size(self):
        print(len(self.sp))

    def clear(self):
        self.sp = list()
        print("ok")

    def exit(self):
        print("bye")
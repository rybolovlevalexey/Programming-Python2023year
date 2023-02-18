class Stack:
    def __init__(self):
        self.sp = list()

    def push(self, elem):
        self.sp.append(elem)
        print("ok")

    def pop(self):
        if len(self.sp) == 0:
            print("error")
        else:
            x = self.sp[-1]
            del self.sp[-1]
            print(x)

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

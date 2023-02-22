class DequeList:
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
class SpisokElem:
    def __init__(self, n):
        self.Value = n
        self.Next = None
        self.Prev = None
class Deque:
    def __init__(self):
        self.Head = None
        #self.Tail = None

    def push_front(self, elem):
        if self.Head is None:
            self.Head = SpisokElem(elem)
        else:
            self.Head.Next = self.Head
            self.Head = SpisokElem(elem)
        print("ok")

    def push_back(self, elem):
        if self.Head is None:
            self.Head = SpisokElem(elem)
        else:
            cur = self.Head
            while cur.Next is not None:
                cur = cur.Next
            cur.Next = SpisokElem(elem)
        print("ok")


deque = Deque()
st = input()
while st != "exit":
    if len(st.split()) == 2:
        deyst, n = st.split()
        eval(f"deque.{deyst}({n})")
    else:
        eval(f"deque.{st}()")
    st = input()
deque.exit()

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
        # self.Tail = None

    def push_front(self, elem):
        if self.Head is None:
            self.Head = SpisokElem(elem)
        else:
            cur = self.Head
            self.Head = SpisokElem(elem)
            self.Head.Next = cur
        print("ok")

    def pop_front(self):
        if self.Head is None:
            print("error")
        else:
            value = self.Head.Value
            self.Head = self.Head.Next
            print(value)

    def pop_back(self):
        if self.Head is None:
            print("error")
        else:
            if self.Head.Next is None:
                print(self.Head.Value)
                self.Head = None
            else:
                cur1 = None
                cur = self.Head
                while cur.Next is not None:
                    cur1 = cur
                    cur = cur.Next
                value = cur.Value
                cur1.Next = None
                print(value)

    def front(self):
        if self.Head is None:
            print("error")
        else:
            value = self.Head.Value
            print(value)

    def back(self):
        if self.Head is None:
            print("error")
        else:
            cur = self.Head
            while cur.Next is not None:
                cur = cur.Next
            value = cur.Value
            print(value)

    def push_back(self, elem):
        if self.Head is None:
            self.Head = SpisokElem(elem)
        else:
            cur = self.Head
            while cur.Next is not None:
                cur = cur.Next
            cur.Next = SpisokElem(elem)
        print("ok")

    def size(self):
        if self.Head is None:
            cnt = 0
        elif self.Head is not None and self.Head.Next is None:
            cnt = 1
        else:
            cur = self.Head
            cnt = 0
            while cur is not None:
                cnt += 1
                cur = cur.Next
        print(cnt)

    def clear(self):
        self.Head = None
        print("ok")

    def exit(self):
        print("bye")


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

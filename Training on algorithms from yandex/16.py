class QueueElement:
    def __init__(self, x):
        self.Value = x
        self.__Prev = None
        self.__Next = None

    @property
    def Prev(self):
        return self.__Prev

    @Prev.setter
    def Prev(self, elem):
        self.__Prev = elem

    @property
    def Next(self):
        return self.__Next

    @Next.setter
    def Next(self, elem):
        self.__Next = elem


class Queue:
    def __init__(self):
        self.Head = None

    def __str__(self):
        cur = self.Head
        if cur is None:
            return "nothing"
        st = str(cur.Value) + "; "
        while cur is not None:
            cur = cur.Next
            if cur is not None:
                st += (str(cur.Value) + "; ")
        return st[:-2]

    def push(self, value):
        if self.Head is None:
            self.Head = QueueElement(value)
        else:
            cur = self.Head
            while cur.Next is not None:
                cur = cur.Next
            cur.Next = QueueElement(value)
            cur_new = cur.Next
            cur_new.Prev = cur
        print("ok")

    def pop(self):
        if self.Head is None:
            print("error")
        else:
            val = self.Head.Value
            self.Head = self.Head.Next
            self.Head.Prev = None
            print(val)

    def front(self):
        if self.Head is None:
            print("error")
        else:
            print(self.Head.Value)

    def size(self):
        if self.Head is None:
            cnt = 0
        else:
            cur = self.Head.Next
            cnt = 1
            while cur is not None:
                cnt += 1
                cur = cur.Next
        print(cnt)

    def clear(self):
        self.Head = None
        print("ok")

    def exit(self):
        print("bye")




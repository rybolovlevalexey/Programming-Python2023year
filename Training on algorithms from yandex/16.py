class QueueElement:
    def __init__(self, x):
        self.Value = x
        self.__Next = None

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
        print("ok")

    def pop(self):
        if self.Head is None:
            print("error")
        else:
            val = self.Head.Value
            self.Head = self.Head.Next
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


queue = Queue()
st = input()
while st != "exit":
    st = st.split()
    if len(st) == 2:
        queue.push(int(st[1]))
    else:
        eval(f"queue.{st[0]}()")
    st = input()
queue.exit()

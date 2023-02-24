class HeapElem:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class Heap:
    def __init__(self):
        self.Head = None
        self.Level = -1
        self.RemaindCnt = 0

    def insert(self, k):
        if self.Head is None:
            self.Head = HeapElem(k)
            self.Level = 0
            self.RemaindCnt = 2**self.Level - 1
        else:
            if self.RemaindCnt >= 2**(self.Level - 1):  # слева нет мест идти направо
                pass
            else:  # слева есть ещё места идти налево
                pass
            #  изменение счётчика оставшихся мест на текущем уровне
            if self.RemaindCnt == 0:
                self.Level += 1
                self.RemaindCnt = 2**self.Level - 1
            else:
                self.RemaindCnt -= 1
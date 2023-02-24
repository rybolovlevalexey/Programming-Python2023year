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


class Heap1:
    def __init__(self):
        self.sp = list()

    def insert(self, k):
        self.sp.append(k)
        pos = len(self.sp) - 1
        while pos > 0 and self.sp[pos] > self.sp[(pos - 1) // 2]:
            self.sp[pos], self.sp[(pos - 1) // 2] = self.sp[(pos - 1) // 2], self.sp[pos]
            pos = (pos - 1) // 2

    def extract(self):
        ans = self.sp[0]
        last = self.sp[-1]
        self.sp[0] = last
        pos = 0
        while pos * 2 + 1 < len(self.sp) - 1:
            max_son_index = pos * 2 + 1
            if self.sp[pos * 2 + 2] > self.sp[max_son_index]:
                max_son_index += 1
            if self.sp[pos] < self.sp[max_son_index]:
                self.sp[pos], self.sp[max_son_index] = self.sp[max_son_index], self.sp[pos]
                pos = max_son_index
            else:
                break
        del self.sp[-1]
        return ans


hp = Heap1()
for i in range(int(input())):
    st = input().strip()
    if " " in st:
        st = st.split()
        hp.insert(int(st[1]))
    else:
        res = (hp.extract())
        print(res)

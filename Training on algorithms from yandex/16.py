class QueueElement:
    def __init__(self, x):
        self.value = x
        self.Prev = None
        self.Next = None

    @property
    def prev(self):
        return self.Prev

    @prev.setter
    def prev(self, elem):
        self.Prev = elem

    @property
    def next(self):
        return self.Next

    @next.setter
    def next(self, elem):
        self.Next = elem


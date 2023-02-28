class NonPositiveError(Exception):
    pass


class PositiveList(list):
    def __init__(self, *args):
        args = filter(lambda x: x > 0, args)
        super().__init__(args)

    def append(self, x) -> None:
        if x > 0:
            super().append(x)
        else:
            raise NonPositiveError


sp = PositiveList(2, 3, 5)
sp.append(1)
print(sp)
sp.append(-1)
class Sherlock:
    def __init__(self, *args):
        self.persons = list(args)

    def __iadd__(self, number):
        self.persons.append(number)

    def __call__(self, *args, **kwargs):
        cnt = len(self.persons)
        mn = set(self.persons)
        for elem in mn:
            if self.persons.count(elem) > cnt // 3:
                return elem
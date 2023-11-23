class Tree:
    def __init__(self, number, chief=None, subords=None):
        self.id = number
        self.chief = chief
        self.subords = subords if subords is not None else list()

    def __str__(self):
        if self.subords is None:
            return f"{self.id}\nРодитель: {self.chief.id}\n"
        sp = list(elem.id for elem in self.subords)
        if self.chief is None:
            return f"{self.id}\n" \
                   f"Дети: {sp}"
        return f"{self.id}\nРодитель: {self.chief.id}\n" \
               f"Дети: {sp}"


n = int(input())
langs = input().split()
st = map(int, input().split())
stack = list()
people = {0: Tree(0)}

for elem in st:
    if elem == 0:
        stack.append(elem)
        continue
    if elem not in stack:
        people[elem] = Tree(elem, people[stack[-1]])
        people[stack[-1]].subords.append(people[elem])
        stack.append(elem)
    else:
        del stack[-1]

for key, value in people.items():
    print(value)
    print()
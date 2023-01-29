import random
class Node:
    def __init__(self, value):
        self.Next = None
        self.Value = value

sp = Node(5)
for i in range(10):
    elem = Node(random.randint(0, 9))
    cur = sp
    while cur.Next is not None:
        cur = cur.Next
    cur.Next = elem
cur = sp
print("Linked list values: ", end=" ")
while cur.Next is not None:
    print(cur.Value, end=" ")
    cur = cur.Next
print(cur.Value)

cur = sp
while cur.Next is not None:
    checker = cur
    print(checker.Value, end=' ')
    while checker.Next is not None:
        print(checker.Value, end=' ')

        if cur.Value == checker.Next.Value and checker.Next is not None:
            checker.Next = checker.Next.Next
        elif cur.Value == checker.Next.Value and checker.Next is None:
            checker.Next = None
        checker = checker.Next
    print()
    cur = cur.Next

cur = sp
while cur.Next is not None:
    print(cur.Value, end=" ")
    cur = cur.Next
print(cur.Value)
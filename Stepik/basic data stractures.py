n = int(input())
books = set()
for i in range(n):
    books.add(input())
for i in range(int(input())):
    if input() in books:
        print("YES")
    else:
        print("NO")
import sys

letters = dict()
for line in sys.stdin:
    for elem in line.strip():
        if elem == " ":
            continue
        if elem in letters:
            letters[elem] += 1
        else:
            letters[elem] = 1
height = max(letters.values())
heading = sorted(letters.keys())
for i in range(height):
    ans = list()
    for key in heading:
        if i + letters[key] >= height:
            ans.append("#")
        else:
            ans.append(" ")
    print(*ans, sep="")
print(*heading, sep="")
import re
import sys


for line in sys.stdin:
    line = line.strip()
    print(re.sub("human", "computer", line))
    #for elem in line.split():
    #    res = re.match(r"^(\w+)*\1", elem)
    #    if res:
    #        print(res, line)
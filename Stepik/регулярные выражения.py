import re
import sys


for line in sys.stdin:
    line = line.strip()
    res = re.sub(r"\b([aA]+)\b", "argh", line, count=1)
    print(res)
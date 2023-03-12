import re
import sys


for line in sys.stdin:
    line = line.strip()
    res = re.sub(r"(\w{2,})", "\\1", line)
    print(res)
import re
import sys


for line in sys.stdin:
    line = line.strip()
    res = re.sub(r"\b(\w{1})(\w{1})(\w*)\b", "\\2\\1\\3", line)
    print(res)
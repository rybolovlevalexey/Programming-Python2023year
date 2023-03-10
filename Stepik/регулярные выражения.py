import re
import sys


for line in sys.stdin:
    line = line.strip()
    if re.match(r"\b(\w\W+)\1\b", line):
        print(line)

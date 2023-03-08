import re
import sys


for line in sys.stdin:
    line = line.strip()
    if len(re.findall(r"z.{3}z", line)) > 0:
        print(line)

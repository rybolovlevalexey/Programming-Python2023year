import re
import sys

for line in sys.stdin:
    line = line.strip()
    pattern = "(\w{1})\\1+"
    print(re.sub(pattern, "\\1", line))
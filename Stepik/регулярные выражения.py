import re
import sys


for line in sys.stdin:
    line = line.strip()
    print(re.sub("\b[Aa]+\b", "argh", line, count=1))

import re
import sys

for line in sys.stdin:
    line = line.strip()
    if len(re.findall(r"\bcat\b", line)) > 0:
        print(line)
import csv

file = open("Crimes.csv", "r")
ans_d = dict()
cfile = csv.DictReader(file)
for row in cfile:
    if row["Date"].split()[0].split("/")[2] != "2015":
        continue
    pr_type = row["Primary Type"]
    ans_d[pr_type] = ans_d.get(pr_type, 0) + 1
for key in ans_d.keys():
    if ans_d[key] == max(ans_d.values()):
        print(key)
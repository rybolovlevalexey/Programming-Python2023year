import zipfile
import os

MY_PATH = "C:\Programming - Python 2023 year\Stepik"
#with zipfile.ZipFile("main.zip", "r") as archiv:
    #archiv.extractall()

ans = list()
for elem in os.walk(MY_PATH + "\main"):
    flag = False
    for one_file in elem[2]:
        if one_file[-3:] == ".py":
            flag = True
            break
    if flag:
        ans.append(elem[0][elem[0].index("main"):])
file_ans = open("answer.txt", "w")
file_ans.write("\n".join(sorted(ans)))
print(*sorted(ans), sep="\n")
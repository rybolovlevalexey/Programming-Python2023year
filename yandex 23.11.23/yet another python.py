name = input()
n = int(input())
files = dict()
cur_path = dict()
for i in range(n):
    st = input()
    j = 0
    for j in range(len(st)):
        if st[j] != " ":
            break
    if len(cur_path) == 0 or j > max(cur_path.keys()):
        if "." in st:
            files[st.strip()] = list(cur_path[key] for key in sorted(cur_path.keys()))
        else:
            cur_path[j] = st.strip()
    else:
        while j < max(cur_path.keys()):
            del cur_path[max(cur_path.keys())]
        if "." in st:
            files[st.strip()] = list(cur_path.values())
        else:
            cur_path[j] = st.strip()
print(f"/{'/'.join(files[name])}/{name}")

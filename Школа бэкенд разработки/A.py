n, m, q = map(int, input().split())  # кол-во дата-центров, кол-во серверов, кол-во событий
data_centers = dict()
for key in range(1, n + 1):
    data_centers[key] = [set(), 0]
for i in range(q):
    st = input()
    if st.startswith("RESET"):
        num = int(st.split()[1])
        data_centers[num][1] += 1
        data_centers[num][0] = set()
    elif st.startswith("DISABLE"):
        num1, num2 = int(st.split()[1]), int(st.split()[2]) - 1
        data_centers[num1][0].add(num2)
    elif st == "GETMAX":
        ans = None
        mx_val = None
        for key, value in data_centers.items():
            result = value[1] * (m - len(value[0]))
            if mx_val is None or result > mx_val:
                mx_val = result
                ans = key
        print(ans)
    elif st == "GETMIN":
        ans = None
        mn_val = None
        for key, value in data_centers.items():
            result = value[1] * (m - len(value[0]))
            if mn_val is None or result < mn_val:
                mn_val = result
                ans = key
        print(ans)

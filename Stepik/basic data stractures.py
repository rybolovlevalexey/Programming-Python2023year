n = int(input())
mn = set()
for i in range(n):
    st = input()
    mn.add(st.lower())
st = input()
if st.lower() in mn:
    print("EXIST")
else:
    print("OK")
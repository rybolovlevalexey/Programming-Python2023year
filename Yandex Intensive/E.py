import sqlite3


def get_result(file_name):
    con = sqlite3.connect(file_name)
    cur = con.cursor()
    ans = dict()
    for cls in range(1, 4):
        alive = list(cur.execute(f'''select passenger_id, parch, survived from titanik where 
        pclass == {cls} and parch > 0 and survived == 1'''))
        cnt = list(cur.execute(f'''select passenger_id, parch, survived from titanik where 
        pclass == {cls} and parch > 0'''))
        res = round(len(alive) / len(cnt), 3)
        ans[str(cls)] = res
    return ans


print(get_result('titanik.db'))

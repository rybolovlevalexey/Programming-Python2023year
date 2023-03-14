n, w = map(int, input().split())
workers = dict()
tasks = list()
for i in range(n):
    ai, ti = map(int, input().split())
    tasks.append([ai, ti, i + 1])
tasks = sorted(tasks)
ans = list()
for elem in tasks:
    ai, ti, i = elem
    ans.append(i)
    worker_index = None
    for key, value in workers.items():
        if value <= ai:
            worker_index = key
            break
    if len(workers) == 0 or worker_index is None:
        workers[len(workers) + 1] = ai + ti
    else:
        workers[worker_index] = ai + ti
print(len(workers))
print(*ans)
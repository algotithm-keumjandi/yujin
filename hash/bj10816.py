m = int(input())
m_list = list(map(int, input().split()))
d = dict()

for i in m_list:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1

n = int(input())
n_list = list(map(int, input().split()))
res  = []

for i in n_list:
    if i in d:
        res.append(d[i])
    else:
        res.append(0)

print(*res)

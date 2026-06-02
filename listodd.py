l = [2,5,6,3,5,6,2,2]
res = []
for i in l:
    if i not in res and l.count(i) % 2 != 0:
        res.append(i)
print(res)
##l = [1,1,1,1,1,3,3,3,2,2]
l = []
n = int(input())
for i in range(n):
    x = int(input())
    l.append(x)
print(l)
res = []
for i in l:
    if i not in res:
        res.append(i)
print(res)
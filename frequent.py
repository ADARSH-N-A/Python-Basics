nums = list(map(int,input().split()))
result = []
d = {}
for i in nums:
    if i not in d:
        d[i] = 1
    else:
        d[i] += 1
print(d)
element,max = 0,0
max2 = 0
for i in d:
    if i > max:
        max2 = max
        max1 = i
        element = i
    elif i > max2 and i!=max:
        max2 = i
        element = i
print(element)
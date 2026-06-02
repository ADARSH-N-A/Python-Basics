l = [1,2,3,4]
print(l)

#insert
l.insert(1,5)
print(l)

#extend
l.extend([5,6,7])
print(l)

#pop
l.pop(2)
print(l)

#Sorting and reversing
l.sort()
print(l)
l.reverse()
print(l)

print(l.index(6))
print(l.count(5))

l2 = [1,2,3]
l3 = l2.copy()
l2.append(4)
print(len(l2))
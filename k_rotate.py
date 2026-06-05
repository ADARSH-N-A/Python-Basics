l = list(map(int,input().split()))
k = int(input("Enter the number of rotation: "))
temp = l[0]

if k < len(l):
    for i in range(len(l)//k):
        l[i], l[k - 1 - i] = l[k - 1 - i], l[i]
    print(l)
    i = k+1
    for i in range(len(l)//2):
        l[i], l[len(l)- 1 - i] = l[len(l) - 1 - i], l[i]
    p = len(l) - k
    for i in range(len(l)//p):
        l[i], l[p - 1 - i] = l[p - 1 - i], l[i]
    temp = l[1]
    l[1] = l[2]
    l[2] = temp
    print(l)
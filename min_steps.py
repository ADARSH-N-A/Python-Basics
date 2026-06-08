count1 = 0
def count(n):
    if n == 1:
        return 0
    elif n % 2 == 0:
        return 1 + count(n // 2)
    else:
        return 1 + min(count(n - 1),count(n + 1))
n = 15
print(count(n))


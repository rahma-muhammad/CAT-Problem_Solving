def anding(n, a, b):
    res = int(a[0]) & int(b[0])
    for i in range(1, n):
        res &= int(a[i])
        res &= int(b[i])

    return res

t = int(input())
for i in range(0, t):
    n = int(input())
    a = list(input().split(' '))
    b = list(input().split(' '))
    print(anding(n, a, b))


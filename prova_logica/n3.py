def blevers(n):
    c = 0
    c1 = 1
    while c1 <= n:
        if n%c1 == 0:
            c = c +1
        c1 = c1 + 1
    print(c)
    print(c1)
    return c%100


n = blevers(15)

print(n)

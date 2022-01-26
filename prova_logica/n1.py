def xpto(v, n):
    s = 0
    i = 0
    while i < n:
        if v[i] % 3 == 0:
            print(v[i])
            s =s + v[i]
        i = i + 1
    return s



a = [23,4,21,3,23]

m1 = xpto(a, 5)

print(m1)
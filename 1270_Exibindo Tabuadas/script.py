#Entradas
v1 = int(input())
v2 = int(input())


if v2 > v1:
    temp = v1
    while temp <= v2:
        for x in range(1,11):
            print( f'{temp} x {x} = {temp*x}')
        print("----------")
        temp = temp +1
elif v1 == v2:
    for x in range(1,11):
        print( f'{v1} x {x} = {v1*x}')
    print("----------")
else:
    print("Nenhuma tabuada no intervalo!")
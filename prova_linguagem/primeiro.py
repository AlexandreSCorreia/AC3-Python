def soma(L):
    impares = 0;
    for i in range(len(L)):
        if L[i] % 2 != 0:
            impares += 1
    return

lista = []
for i in range(10):
    x = int(input('Numero: '))
    lista.append(x)
print(f'A soma dos itens impares da lista é {soma(lista)}')
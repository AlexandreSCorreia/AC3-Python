entrada = int(input())

notas = 0
continuar = True
nota_atual = []
ajuste = []

#continuar = False       
#print(*valores)

while continuar:
    if len(nota_atual) <= entrada -1:
         notas = float(input())
         nota_atual.append(notas)
    elif len(nota_atual) > entrada -1 and len(ajuste) <= entrada -1:
        notas = float(input())
        ajuste.append(notas)
    else:
        continuar = False
        print(f'NOTAS ALTERADAS: {0}')
        print(*nota_atual)
        print(*ajuste)
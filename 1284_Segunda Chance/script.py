entrada = int(input())

notas = 0
continuar = True
nota_atual = []
ajuste = []
nota_final = []

notas_alteradas = 0

while continuar:
    if len(nota_atual) <= entrada -1:
         notas = float(input())
         nota_atual.append(notas)
    elif len(nota_atual) > entrada -1 and len(ajuste) <= entrada -1:
        notas = float(input())
        ajuste.append(notas)
    else:
        continuar = False
        cont = 0
        while cont < entrada:
            
            if ajuste[cont] == 10 and nota_atual[cont] != 10:
                if (nota_atual[cont]  + 2) <= 10:
                    nota_final.append(nota_atual[cont] + 2)
                else:
                     nota_final.append(10)
                notas_alteradas += 1
            else:
                nota_final.append(nota_atual[cont])
            cont += 1
        cont = 0
        print(f'NOTAS ALTERADAS: {notas_alteradas}')
  
        while cont < entrada:
            simbolo = '-'
            if nota_atual[cont] != nota_final[cont]:
                simbolo = '*'
            print(f'{simbolo}({(cont + 1):03d}) original: {nota_atual[cont]:05.2f} | final: {nota_final[cont]:05.2f}')
            cont += 1

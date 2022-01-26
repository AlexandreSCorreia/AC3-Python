def get_canais(quantidade):
    canais = []
    continuar = True
    cont = 0
    while continuar:
        if cont < quantidade:
            canal = input().split(';')
            canais.append(canal)
        else:
            continuar = False
        cont += 1
    return canais

def calcula_monetizacao(canal,com_premium,sem_premium):
    bonus = 0
    inscritos = int(canal[1]) // 1000
    monetizacao = float(canal[2])

    if canal[3] == 'sim':  
        bonus = monetizacao + (inscritos * com_premium)          
    else:
        bonus = monetizacao + (inscritos * sem_premium)
    return bonus    

def main():
    quant_canais = int(input())
    canais = get_canais(quant_canais)
    com_premium = float(input())
    sem_premium = float(input())
  
    print('-----')
    print('BÔNUS')
    print('-----')   

    for canal in canais:
       bonus = calcula_monetizacao(canal,com_premium,sem_premium)
       print(f'{canal[0]}: R$ {bonus:.2f}')
       
main()
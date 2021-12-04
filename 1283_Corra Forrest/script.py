entrada = int(input())
continuar = True
valores = []
media = 0

def calc_media():
    total = 0
    for x in valores:
        total += x
    return total / len(valores)

while continuar:
    if entrada < 0:
        continuar = False
        media = calc_media()
        print(f'MEDIA: {media:.2f}')
        for x in valores:
           if x < media:
               print(x)
    elif entrada > 0:
        valores.append(entrada)
        entrada = int(input())
       
# beecrowd | 1269
# Carrinho de compras

itens = []
ativo = True

#Funções
def bubble_sort(lista):
    tamanho = len(lista)
    while tamanho > 1:
        empurrar(lista,tamanho)
        tamanho = tamanho -1
    return

def empurrar(lista, tamanho):
    i = 0
    while i < tamanho - 1:
        if lista[i] > lista[i+1]:
            troca(lista,i,i+1)
        i = i + 1        
    return
           
def troca(v,p1,p2):
    temp = v[p1]
    v[p1] = v[p2]
    v[p2] = temp
    return

def busca_binaria(valor, sequencia):
    inicio = 0
    fim = len(sequencia) -1
    while inicio <= fim:

        meio = (inicio + fim) // 2

        if valor == sequencia[meio]:
            return meio
        elif valor < sequencia[meio]:
            fim = meio - 1
        else:
            inicio = meio + 1

    return None

#Entrada
for x in  input().split():
    itens.append(int(x))

#Processo
while ativo:
    nova_entrada = input().split()
    if nova_entrada[0] == "encerrar":
        bubble_sort(itens)
        print(*itens)
        ativo = False
    elif nova_entrada[0] == "adicionar":
           itens.append(int(nova_entrada[1]))
    elif nova_entrada[0] == "remover":
            value = busca_binaria(int(nova_entrada[1]), itens)
            if value == None:
                print(f'código {nova_entrada[1]} não encontrado')
            else:
                del(itens[itens.index(int(nova_entrada[1]))])
    elif nova_entrada[0] == "exibir":
        bubble_sort(itens)
        print(*itens)
            




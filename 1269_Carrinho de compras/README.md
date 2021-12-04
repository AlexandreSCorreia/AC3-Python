<div align="center"> 
   <small> beecrowd | 1269 </small>
   <h1> Carrinho de compras </h1>
</div>

Você está criando um site para uma loja virtual e precisa guardar os itens que os usuários adicionam em seu carrinho. Cada item é representado no sistema por um código numérico, isto é, um número inteiro que é capaz de identificá-lo unicamente. Como solução inicial, você decidiu guardar os itens adicionados ao carrinho em uma lista e, para testar o seu programa, implementou alguns comandos básicos para simular uma interação do usuário com o sistema:

- adicionar: inclui o código de um novo produto à lista;
- remover: remove o código de um produto da lista;
- exibir: exibe os itens da lista em ordem crescente;
- encerrar: exibe os itens da lista, de modo idêntico ao comando exibir, e encerra o programa.

A primeira linha poderá conter uma lista de inteiros separados por espaços, representando produtos que já estavam no carrinho, por exemplo, de uma sessão anterior que o usuário iniciou mas não finalizou a compra. Você deve receber essa lista e inicializar o carrinho de compras já com os códigos dessa lista, que devem ser números inteiros.

Caso não haja nenhum produto salvo de uma sessão anterior, essa primeira linha será uma linha em branco, sem nenhum texto ou caractere.


## Entrada

- A primeira linha poderá conter números inteiros separados por espaço ou ser uma linha vazia;

- As próximas linhas serão os comandos citados anteriormente, sendo que linhas com comandos "adicionar" e "remover" também possuem um valor à direita do comando, que representa o código do produto, note que há um espaço entre o comando e o código;

- A entrada sempre é encerrada com o comando "encerrar".

## Saída

A saída deve conter:

- Os códigos dos produtos que estão no carrinho separados por um espaço e de acordo com a execução dos comandos "exibir" e "encerrar";

- A mensagem "código <código> não encontrado" (sem aspas), quando o comando remover for executado com um código que não esteja no carrinho. Substitua <código> pelo código não encontrado, conforme os casos de teste de exemplo.

Observação: Lembre-se de não exibir texto no input.

<img src="source_readme/teste01.png" min-width="400px" max-width="400px" width="400px" align="center" alt="teste01">





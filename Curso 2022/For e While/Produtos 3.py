'''
Lembram do aplicativo de mercado que fizemos na última aula?

Vamos refazer o código pedindo os produtos e valores usando o laço while. 
Ao pedir um produto, o cliente pode adicionar um novo produto ou só dar enter para finalizar o pedido e receber o valor total da compra.

Regra: NÃO USE BREAK

Dica: se só dermos um enter no input, o python recebe uma string vazia "".
'''

total = 0
print('Para terminar a compra, tecle "enter"')
nome = input('Digite o nome do produto: ')
valor = float(input('Digite o valor do produto: '))
total = total + valor

while nome != "":
  nome = input('Digite o nome do produto: ')
  if nome != "":
    valor = float(input('Digite o valor do produto: '))
    total = total + valor
  
print('A soma total dos produtos comprados é R$%.2f'%total)

'''
Ainda pensando no aplicativo, crie um algoritmo em Python em que a pessoa não precisa inserir o número de produtos que está comprando. Considere que o algoritmo consegue armazenar no máximo 1000 produtos.

Dica: você precisa perguntar para o usuário se ele deseja continuar ou se deseja fechar a compra.
'''

total = 0
print('Para terminar a compra, digite "encerrar"')

for i in range(1000):
  nome = input('Digite o nome do produto: ')
  if nome == "encerrar":
    break

  else:
    valor = float(input('Digite o valor do produto: '))
    total = total + valor
  
print('A soma total dos produtos comprados é R$%.2f'%total)

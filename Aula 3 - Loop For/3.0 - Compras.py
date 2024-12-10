'''
Você está criando um aplicativo para auxiliar pessoas na hora de fazer compras no mercado. Neste aplicativo a pessoa pode inserir o número de produtos que está comprando e depois o nome de cada produto e o valor. No final, apresente para a pessoa a soma total da compra.
'''
# 1. Pedir o número de produtos.
# 2. Pedir nome e valor n vezes.
# 3. Apresente a soma total.

quantidade = int(input('Digite o número de produtos que está comprando: '))

total = 0   # não pode estar no for porque senão o valor será zerado a cada repetição.

for i in range(quantidade):
  nome = input('Digite o nome do produto: ')
  valor = float(input('Digite o valor do produto: '))
  total = total + valor

print('A soma total dos produtos comprados é R$%.2f'%total)

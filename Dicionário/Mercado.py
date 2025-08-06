print('AVISO! Digite "fim" para terminar a consulta de preços.')

mercado = {'arroz': 18.00,
          'feijão' : 7.99,
          'alface' : 1.98,
          'batata' : 4.59,
          'macarrão' : 2.99}

disponiveis = []
indisponiveis = []
carrinho = []
total = []
total_final = 0

while True:
  produto = input('\nDigite o nome do produto desejado: ')
  if produto in mercado:
    print('O preço de {} é R$ {}.'.format(produto, mercado[produto]))
    disponiveis.append(produto)
    adicionar = input('Adicionar produto ao carrinho? ')
    if adicionar == 'sim':
      quantidade = int(input('Quantos? '))
      for i in range(quantidade):
        carrinho.append(produto)
      total_produto = quantidade * mercado[produto]
      total.append(total_produto)

  elif produto == "fim":
    break

  else:
    print('Que pena! Não temos esse produto.')
    indisponiveis.append(produto)

for total_produto in total:
  total_final = total_final + float(total_produto)

print('\nHá {} produtos no seu carrinho. O total é de R$ {:.2f}'.format(len(carrinho), total_final))

print('\n{} produtos disponíveis no mercado e {} produtos indisponíveis foram consultados.'.format(len(disponiveis), len(indisponiveis)))

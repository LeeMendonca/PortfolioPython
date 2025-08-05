'''
Sua amiga Gabi está sempre reclamando que esquece de algo quando vai fazer compras. Para ajudá-la, crie um programa onde ela possa criar uma lista de compras virtual, adicionar
à lista os itens que precisa e ter todos eles impressos ao final.

→ Quando ela digitar "fim", o algoritmo imprime a lista de compras;
→ Cada item da lista deve ser impresso em uma linha.
'''

itens = []

while True:
  i = input('Itens: ')
  if i == "fim":
    break
  itens.append(i)

print('\n')

print('LISTA DE COMPRAS')
for n in range (len(itens)):
  print('-', itens[n])

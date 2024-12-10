'''
Escreva um algoritmo que pede para uma pessoa inserir um número.
Se este número for maior que zero, imprima
 "é maior que zero".
Se este número for menor que zero, imprima
 "é menor que zero".
Se o número for zero, imprima "ZERO!"
'''
n = int(input('Digite um número: '))

if n > 0:
  print('É maior que zero')

elif n < 0:
  print('É menor que zero')

else:
  print('ZERO!')

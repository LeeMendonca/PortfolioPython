'''
Crie um algoritmo que peça para o usuário entrar com números aleatórios até que ele insira um número negativo usando WHILE.
'''
n = 0

while n >= 0:
 n = float(input('Digite um número aleatório: '))
 if n < 0:
   break

print('Acabou o código')
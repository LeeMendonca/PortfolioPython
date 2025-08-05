'''
Exercício 1.1 - Amigos
'''

nome = input('Digite o nome do amigo(a): ')
local = input('Digite o local onde se conheceram: ')
dia = int(input('Qual o dia de nascimento dele(a)? '))
mes = int(input('E o mês? '))
niver = str(dia) + '/' + str(mes)
print('Amigo(a): {} | {} | {}\n'.format(nome, local, niver))

while nome != '':
  nome = input('Digite o nome do amigo(a): ')
  if nome != '':
    local = input('Digite o local onde se conheceram: ')
    dia = int(input('Qual o dia de nascimento dele(a)? '))
    mes = int(input('E o mês? '))
    niver = str(dia) + '/' + str(mes)
    print('Amigo(a): {} | {} | {}\n'.format(nome, local, niver))

print('Fim do programa')

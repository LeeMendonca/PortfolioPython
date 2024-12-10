'''
Exercício 1 - Amigos

Pensando no seu facebook, como você adicionaria seus amigos no seu perfil?
Crie um algoritmo em Python que recebe o nome de 3 amigos,
de onde você conhece cada um deles,
o dia e o mês que esse amigo faz aniversário (considere o mês como um número).
'''

a1 = input('Digite o nome do primeiro amigo: ')
local1 = input('Digite o local onde se conheceram: ')
dia1 = int(input('Digite o dia do aniverário do primeiro amigo: '))
mes1 = int(input('Digite o mês do aniverário do primeiro amigo: '))
niver1 = str(dia1) + '/' + str(mes1)
# É necessário alterar o tipo da variável, individualmente, ao usar o simbolo "+" para concatenar.

a2 = input('Digite o nome do segundo amigo: ')
local2 = input('Digite o local onde se conheceram: ')
dia2 = int(input('Digite o dia do aniverário do segundo amigo: '))
mes2 = int(input('Digite o mês do aniverário do segundo amigo: '))
niver2 = str(dia2) + '/' + str(mes2)

a3 = input('Digite o nome do terceiro amigo: ')
local3 = input('Digite o local onde se conheceram: ')
dia3 = int(input('Digite o dia do aniverário do terceiro amigo: '))
mes3 = int(input('Digite o mês do aniverário do terceiro amigo: '))
niver3 = str(dia3) + '/' + str(mes3)

print('Amiga 1: '+ a1 + ' | ' + local1 + ' | ' + niver1)
print('Amiga 2: '+ a2 + ' | ' + local2 + ' | ' + niver2)
print('Amiga 3: '+ a3 + ' | ' + local3 + ' | ' + niver3)

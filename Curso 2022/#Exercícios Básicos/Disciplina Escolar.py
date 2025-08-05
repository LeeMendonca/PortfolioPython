'''
Exercício 3 - Disciplica Escolar

Escreva um algoritmo para cadastrar e imprimir na tela os
dados de uma disciplina escolar: nome da matéria, descrição,
frequência e média mínima para aprovação.

'''

nome = input('Nome da matéria: ')
descricao = input('Descrição: ')
frequencia = input('Frenquência: ')
media = float(input('Média mínima para aprovação: '))

print('\n')

print('{}: {}\n{}% | {:.1f}'.format(nome, descricao, frequencia, media))

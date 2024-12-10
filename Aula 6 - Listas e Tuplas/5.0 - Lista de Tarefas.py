'''
Marcela irá prestar vestibular este ano e tem muitos conteúdos para estudar e atividades para fazer ao longo de um dia. Ajude Marcela a se organizar criando um programa para que ela diariamente insira sua lista de tarefas.

Crie um algoritmo em Python para que ela possa digitar, item por item, as tarefas que precisa fazer em um dia. Quando ela digitar "fim", o algoritmo printa a quantidade de tarefas inseridas.
'''

tarefas = []

tarefa = input('Insira a primeira tarefa do dia: ')

while tarefa != 'fim':
  tarefa = input('Insira a próxima tarefa: ')
  tarefas.append(tarefa)

print('\nQuantidades de tarefas do dia: {}\n\n'.format(len(tarefas)))

# ou

tarefas = []

while True:
  t = input('Tarefas: ')
  if t == '':
    break
  tarefas.append(t)

print('\nQuantidades de tarefas do dia: {}\n\n'.format(len(tarefas)))

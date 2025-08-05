'''
Atividade 16

Marcela irá prestar vestibular este ano e tem
muitos conteúdos para estudar e atividades para
fazer ao longo de um dia. Ajude Marcela a se
organizar criando um programa para que ela
diariamente insira sua lista de tarefas.

Crie um algoritmo em Python para que ela possa
digitar, item por item, as tarefas que precisa
fazer em um dia. Quando ela digitar "fim", o
algoritmo printa a quantidade de tarefas inseridas.

'''

print("=== Lista de Tarefas ===\nDigite 'fim' para encerrar\n")

tarefas = []

while True:
    item = input("Qual tarefa deseja adicionar? ")

    if item == "fim":
        break
    else:
        tarefas.append(item)

print(tarefas)
print(f"Sua lista tem {len(tarefas)} itens.")
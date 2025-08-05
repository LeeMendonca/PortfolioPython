'''
Atividade 1

O festival de música Pie in the Sky acontece todo ano.
Você e suas amigas finalmente acreditam que têm idade suficiente para poder ter 
acesso ao evento.

Para ter acesso liberado ao Pie in the Sky, as visitantes precisam formar um 
grupo de pelo menos 4 pessoas, que juntas somam no mínimo 77 anos.

Faça um programa que leia o nome e a idade de cada uma das suas amigas e
verifique se vocês conseguirão entrar no evento.

'''

print("=== Festival Pie in the Sky ===\n")

while True:
    pessoas = int(input("Digite o número de integrantes do seu grupo: "))
    if pessoas < 4:
        print("O grupo deve ter ao menos 4 pessoas!\n")
    else:
        break

soma = 0

for i in range(pessoas): # 0 é um inicializador padrão
    print(f"\nIntegrante {i+1}")
    nome = input("Digite seu nome: ")
    idade = int(input("Digite a idade: "))
    soma += idade 
        
if soma >= 77:
    print("\nEba! Esse ano você e suas amigas poderão participar do Pie in the Sky!")
else:
    print("\nInfelizmente, esse ano você e suas amgias não poderão participar do Pie in the Sky!")
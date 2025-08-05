'''
Atividade 2

No hortifruti que Marina trabalha existem 150
produtos disponíveis para as clientes. Para entender
um pouco mais sobre o perfil de compra das clientes,
o pessoal de dados da empresa da Marina resolveu
verificar quantos produtos cada cliente compra em
cada pedido.

Utilize as estruturas break e for para ajudar Marina
a criar um programa que tenha como entrada os
produtos que cada cliente compra por pedido e que

retorne quantos produtos compraram.
'''

print("=== Hortifruti ===")

qtd = 0
lista = []

for i in range(150):
    produto = input("Qual produto você comprou? ")
    
    if produto == "":
        break
    else:
        if produto not in lista:
            lista.append(produto)
        
print(f"A cliente comprou {len(lista)} produtos diferentes!")
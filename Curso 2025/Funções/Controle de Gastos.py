'''
Atividade 7

Sofia quer controlar seus gastos mensais. Se o total ultrapassar R$3.000, 
ela considera que precisa reduzir despesas.

Crie uma função analise_gastos(gastos) que recebe uma lista de valores gastos
e retorna o total e uma mensagem: "Gastos dentro do planejado." ou "Atenção:
gastos acima do limite!"
'''

print("=== Controle de Gastos ===\n")

gastos = []

def analise_gastos(gastos):
    
    soma = 0
    for i in gastos:
        soma += i
    
    print(f"\nVocê gastou R${soma:,.2f} este mês.")
    
    if soma >= 3000:
        print("Atenção: gastos acima do limite!")
    else:
        print("Gastos dentro do planejado!")

while True:
    valor = input("Digite o valor gasto: ")
    
    if valor == "":
        break
    
    gastos.append(float(valor))
    
analise_gastos(gastos)
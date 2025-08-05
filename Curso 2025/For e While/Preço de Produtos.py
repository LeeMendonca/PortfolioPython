'''
Atividade 18 - Aula 3 Barbara Liskov - pg 153

Lucy e Ana estão em processo de mudança para uma nova república
universitária e, pela primeira vez, farão compras no mercado local.

Na tabela ao lado temos alguns itens da lista de compras com
os preços do folheto promocional.

PRODUTO PREÇO
Arroz R$18,00
Feijão R$7,99
Alface R$1,98
Batata R$4,59 (1 kg)
Macarrão R$2,99

Elabore um programa para ajudar Lucy e Ana a checar os preços
dos produtos com um dicionário. Elas devem digitar o nome do
produto e receber seu preço. Ao digitar fim o programa pára de rodar.

'''
tabela = {
    "Arroz": 18.00,
    "Feijão": 7.99,
    "Alface": 1.98,
    "Batata": 4.59,
    "Macarrão": 2.99
}

while True:
    produto = input("Digite o nome do produto: ")
    
    if produto == '':
        break
    if produto in tabela:
        print(f"Preço: R${tabela[produto]}")
    else:
        print("Produto não encontrado!")

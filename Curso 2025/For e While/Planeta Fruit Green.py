'''
Atividade 4

Daina e  Mayara moram no planeta Fruit Green e vieram passar uma temporada na 
Terra. Trouxeram algumas economias na moeda local de Fruit Green, conhecida como
"fruit" para conseguir pagar a estadia na Terra. Sabendo que:

- Para passar 1 dia na Terra cada uma delas gasta 57 reais
- Cada fruit vale 10 reais na Terra
- Elas pretendem passar 13 dias na Terra
- Daiana e Mayara juntas trouxeram 1000 fruits

Elabore um programa para ajudar Daiana e Mayara a calcular se vão conseguir
passar os 13 dias por aqui ou se precisarão voltar mais cedo.
'''
print ("=== Hospedagem para Fruit Greens ===\n")

total = 1000 * 10 # fazendo a conversão de fruits para reais
dias = 1
custo = 0 

while dias <= 13:
    custo += 57*2 # gasto diário por pessoa = 57; quantidade de pessoas = 2.
    dias += 1

restante = total - custo
print(f"Daiana e Mayara gastaram R${custo:,.2f}.")

if custo <= total:
    print(f"Elas ainda tem R${restante:,.2f}, logo vão conseguir passar os 13 dias aqui na Terra!")
else:
    print("Diana e Mayara precisarão voltar mais cedo para Fruit Green :(")
'''
Atividade 17

A professora de PI (Processamento da Informação) armazena as notas de uma aluna
em uma lista. Você consegue escrever um algoritmo que calcula a média das notas?

Utilize a seguinte lista de notas: [3.4, 6.6, 8, 9, 10, 9.5, 8.8, 4.3]

'''
notas = [3.4, 6.6, 8, 9, 10, 9.5, 8.8, 4.3]

soma = 0

for i in notas:
    soma += i

media = soma/len(notas)
print(f"Média: {media:,.2f}")

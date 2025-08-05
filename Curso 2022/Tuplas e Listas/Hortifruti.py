'''
No hortifruti que Marina trabalha existem 150 produtos disponíveis para as clientes.

Para entender um pouco mais sobre o perfil de compra das clientes, o pessoal de dados da empresa da Marina resolveu verificar quantos produtos diferentes cada cliente compra em cada pedido.

Utilize as estruturas break e for para ajudar Marina a criar um programa que tenha como entrada os produtos que cada cliente compra por pedido e que retorne quantos produtos diferentes compraram.
'''

lista = []

for i in range(150):
  produto = input('Qual produto você comprou? ')
  if produto == '':
    break
  elif produto not in lista:
    lista.append(produto)

print('Você comprou {} produtos diferentes.'.format(len(lista)))

# Nesse caso, se o cliente inserir o mesmo produto duas vezes, só será contada uma vez.
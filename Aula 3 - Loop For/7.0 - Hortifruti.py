'''
No hortifruti que Marina trabalha existem 150 produtos disponíveis para as clientes.

Para entender um pouco mais sobre o perfil de compra das clientes, o pessoal de dados da empresa da Marina
resolveu verificar quantos produtos diferentes cada cliente compra em cada pedido.

Utilize as estruturas break e for para ajudar Marina a criar um programa que tenha como entrada os produtos
que cada cliente compra por pedido e que retorne quantos produtos diferentes compraram.
'''
# Como existem 150 produtos, podemos criar um for que se repete no máximo 150 vezes e pergunta os produtos que a cliente comprou.
qtd_diferentes_produtos = 0

# Quantidade total de produtos disponíveis
for i in range (150):
  produto = input('Qual produto você comprou? ')

# Nesse caso, para parar o programa, basta a cliente dar um enter como entrada.
  if produto == "":
    break
  else:
    qtd_diferentes_produtos = qtd_diferentes_produtos + 1

print('Você comprou {} produtos diferentes.'.format(qtd_diferentes_produtos))

# Nesse caso, só funciona se a pessoa souber que não pode digitar o mesmo produto novamente.
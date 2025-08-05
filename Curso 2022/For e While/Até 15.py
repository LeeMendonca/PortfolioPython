'''
Crie um programa que peça para o usuário inserir números aleatórios. O algoritmo deve parar quando a soma for maior que 15.
'''

soma = 0

while soma <= 15:
  n = float(input('Digite um número aleatório: '))
  soma = soma + n
  print(soma) # linha desnecessária, mas útil, caso queria saber o passo a passo da soma.
  if soma > 15:
    break

'''
Crie um programa que lê as idades e alturas de alguns alunos. A condição de parada é a altura = 0.
Em seguida, o programa deve informar quantos alunos com mais de 13 anos possuem altura inferior à 1.5.
'''

altura = 1
contador = 0

while altura != 0:
  altura = float(input('Digite a altura do aluno: '))
  if altura == 0:
    break
  idade = int(input('Digite a idade do aluno: '))
  if idade > 13 and altura < 1.5:
    contador = contador + 1 

print(contador, 'alunos têm mais de 13 anos e possuem altura inferior à 1.5m')

'''Ajude a professora Anna a completar o relatório do seu curso de Python. Ela precisa informar quantas das estudantes irão receber o certificado ao fim do curso.

Para receber o certificado, a aluna precisa ter presença no mínimo em 4 das 5 aulas.

Ela informa que a turma possui 10 estudantes com as seguintes quantidades de faltas:

[0,3,0,0,0,1,2,1,1,0]

Faça um programa que imprime quantas alunas receberão o certificado
'''

# faltas = input('Insira o número de faltas de cada estudante: ')

faltas = [0,3,0,0,0,1,2,1,1,0]
contagem = 0

for i in range(10):

  if faltas[i] > 1:
    print('Aluna', i+1, ': não receberá o certificado')
  else:
    contagem = contagem + 1 
    print('Aluna', i+1, ': receberá o certificado')
  
print('\nTotal:', contagem, 'alunas receberão o certificado.')
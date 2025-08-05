'''
Após Anna escrever a lista com as notas das alunas, ela percebeu que cometeu dois erros na conferência da lista de presença. A terceira aluna da lista teve na verdade
duas faltas ao invés de zero e a oitava aluna teve três faltas ao invés de uma.

Escreva um código simulando essa alteração na lista, utilizando a alteração de itens por índice.
'''

faltas = [0,3,0,0,0,1,2,1,1,0]
contagem = 0

faltas[2] = 2 
# faltas[2] faz menção à terceira aluno, pois o índice da lista começa no zero.
faltas[7] = 3

for i in range(10):

  if faltas[i] > 1:
    print('Aluna', i+1, ': não receberá o certificado')
  else:
    contagem = contagem + 1 
    print('Aluna', i+1, ': receberá o certificado')
  
print('\nTotal:', contagem, 'alunas receberão o certificado.')
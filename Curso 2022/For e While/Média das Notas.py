'''
Atividade 5.1 - Média das Notas - Usando Laço
'''
alunas = int(input('Quantidade de alunas que realizaram a prova: '))
provas = int(input('Quantidade de provas que foram aplicadas para cada aluna: '))

media = 0

print('\nDigite os nomes e as notas de cada aluna.')

for a in range (1, alunas+1):
  nome = input('Nome: ')
  
  for p in range (1, provas+1):
    frase = 'Nota da P' + str(p) + ' de ' + str(nome) + ': '
    prova = int(input(frase))
    media = (media + prova)
  media = media / provas
  print('A média das provas de ' + nome + ' é: {:.2f}\n'.format(media))
  media = 0

print('Fim do programa.')    

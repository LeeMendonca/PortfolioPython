'''
A professora de PI (Processamento da Informação), Denise, armazena as notas de uma aluna em uma lista. Você consegue escrever um algoritmo que calcula a média das notas?
'''

notas = []
soma = 0
n = 0

print('Digite enter para parar de inserir notas.\n')

while n != '':
  n = (input('Digite a nota da aluna: '))
  if n != '':
    notas.append(n)
  
for n in notas:
  soma = soma + float(n)

# atalho → media = sum(notas) / len(notas) → não funcionaria com str(n)
media = soma / len(notas)
print('\nA média das notas é {:.1f}'.format(media))

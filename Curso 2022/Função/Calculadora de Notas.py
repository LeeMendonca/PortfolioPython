# Calculadora de notas
print('CALCULADORA DE NOTAS\n\nDê enter para encerrar.\n')

def soma(lista):
  total = 0
  for item in lista:
    total = total + item
  return total


def media(lista):
  return soma(lista) / len(lista)

def conceito(lista):
  if media(lista) < 5:
    c = 'F'
  elif media(lista) < 6.5:
    c = 'D'
  elif media(lista) < 7.5:
    c = 'C'
  elif media(lista) < 9.0:
    c = 'B'
  else:
    c = 'A'

  return c

notas = []

while True:
  n = input('Digite a nota da aluna: ')
  if n == '':
    break
  notas.append(float(n))

print('\nMédia notas: {:.2f}'.format(media(notas)))
print('Conceito:', conceito(notas))

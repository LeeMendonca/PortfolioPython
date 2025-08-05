'''
Você lembra que ajudou a Profa Denise com o cálculo das notas finais da disciplina de PI?

CONCEITO ..... NOTA (n)
A ............ n>= 9.0
B ............ 7.5 <= n < 9.0
C ............ 6.5 <= n < 7.5
D ............ 5.0 <= n < 6.5
F ............ n < 5

Agora, ela precisa de ajuda para converter as notas para os conceitos da UFABC de acordo com a tabela:

Como você construiria esse programa utilizando uma função em Python?
'''

def soma(lista):
    total = 0
    for item in lista:
      total = total + item
    return total

def media(lista):
    return soma(lista)/len(lista)

def conceito(lista):
    if soma(lista)/len(lista) < 5:
      c = 'F'
    elif soma(lista)/len(lista) < 6.5:
      c = 'D'
    elif soma(lista)/len(lista) < 7.5:
      c = 'C'
    elif soma(lista)/len(lista) < 9.0:
      c = 'B'
    else:
      c = 'A'
    
    return c

notas1 = [7, 5.8, 9]
notas2 = [10, 6.9, 10]
notas3 = [4.5, 6.2, 7.4]

print('Média notas 1: {:.2f}'.format(media(notas1)))
print('Conceito:', conceito(notas1))
  
print('\nMédia notas 2: {:.2f}'.format(media(notas2)))
print('Conceito:', conceito(notas2))

print('\nMédia notas 3: {:.2f}'.format(media(notas3)))
print('Conceito:', conceito(notas3))

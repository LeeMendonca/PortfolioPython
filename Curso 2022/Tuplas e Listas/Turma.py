'''
A professora Cláudia deseja saber quantos nomes diferentes existem em sua turma.

Faça um programa que leia os nomes de cada aluna e imprima ao final os nomes diferentes existentes na turma e quantos são os nomes diferentes.

Saída:
::: LISTA DE NOMES NA TURMA :::
- Nome 1
- Nome 2
- Nome 3
...
> A turma possui X nomes diferentes
'''

nomes = set()

while True:
  n = input('Digite o nome da aluna: ')
  if n == '':
    break
  nomes.add(n)

print('\n::: LISTA DE NOMES NA TURMA :::')

for n in nomes:
  print('-', n)

quantidade = len(nomes)
print('\nA turma possui {} nomes diferentes.'.format(quantidade))

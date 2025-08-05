'''
Escreva um algoritmo para ler 2 valores e se o segundo valor informado for ZERO, deve ser lido um novo valor, ou seja, para o segundo valor não pode ser aceito o valor zero. Por fim, imprima o resultado da divisão do primeiro valor lido pelo segundo valor lido.
'''

v1 = float(input('Digite um valor: '))
v2 = float(input('Digite outro valor: '))

while v2 == 0:
  print('O segundo valor deve ser diferente de ZERO!')
  v2 = float(input('Digite o segundo valor: '))

resultado = v1 / v2
print('O resultado da divisão do primeiro valor pelo segundo valor é', resultado)

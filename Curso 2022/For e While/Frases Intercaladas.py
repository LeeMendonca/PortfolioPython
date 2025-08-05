'''
Crie um algoritmo que imprima 10 frases, de forma intercalada (5 vezes uma e 5 vezes a outra), as frases:
"Python é maravilhoso"
"Mulher na computação não é bug" 
'''

for i in range(5):
  print('Python é maravilhoso')
  print('Mulher na computação não é bug')

print('\n#Outra forma:\n')

frase1 = 'Python é maravilhoso'
frase2 = 'Mulher na computação não é bug'

for i in range(10):
  if i % 2 == 0:
    print(frase1) 
  else:
    print(frase2)

print('\nSe houver dúvida do que o i está fazendo, basta imprimi-lo sozinho. Exemplo:\n')
for i in range(0,10,2):
  print(i)

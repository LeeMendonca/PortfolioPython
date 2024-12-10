'''
Escreva um algoritmo que solicite à cliente entrar com
um número de 1 a 10 e o algoritmo imprime a tabuada de 0 a 10 do número escolhido.
Imprima neste formato:
0 x 2 = 0
1 x 2 = 2
2 x 2 = 4
3 x 2 = 6

Passos
1. Pedir um número de 1 a 10.
2. for que vai rodar 10 vezes -> range(11).
3. Imprimir a tabuada.
'''

n = int(input('Digite um número de 1 a 10: '))

for i in range(11):
  mult = i * n
  print(str(i), ' x ', str(n),' = ', mult)

print('Fim do programa.')

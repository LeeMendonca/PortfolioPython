'''
Crie um algoritmo que possui um laço for em um range de 1 a 16,
mas que pare sua execução se o valor da iteração ( i ) for maior que 10 e par.

Dica: para saber se um número é par, você pode usar o operador aritmético %.
Lembram o que ele fazia?

'''

for i in range(1,17):
  print(i)
  if i > 10 and i % 2 == 0: 
  #Se i % 2 == 0, temos de i é par. Se i % 2 == 1, temos que i é ímpar.
    break

print('O valor da iteração (i) é maior do que 10 e par, por isso, break.')
print('Fim do programa.')

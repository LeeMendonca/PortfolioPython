'''
Range

Intervalo de números que nós definimos e que possui um início e um fim.
É representado da seguinte maneira: range(valor_inicial,valor_final)

O valor final é utilizado para marcar o fim e ele não é utilizado.
No exemplo abaixo,  o intervalo inicia em 1 e finaliza em 11, porém, veja que o número 11 não aparece no resultado.
range(1,11) = 1,2,3,4,5,6,7,8,9,10 
Outro exemplo: range(0,7) = 0,1,2,3,4,5,6

Quando o primeiro valor do range é 0, podemos omitir o zero e obtemos o mesmo resultado.
range(0,7) = range(7)

Para um número n, usa-se:
range(0,n+1)
'''

n = int(input('Insira um número inteiro:'))

for i in range(1,n+1): #i é apenas uma variável que vai assumir os valores do range, quando entramos no for.
  print(i)

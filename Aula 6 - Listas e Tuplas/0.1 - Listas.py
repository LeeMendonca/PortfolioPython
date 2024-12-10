### LISTAS ###

'''
Uma lista é uma sequência de valores que são referenciados por um mesmo nome de variável. Os valores em um lista são chamados de elementos, ou, algumas vezes, de itens.
'''
lista1 = [10, 25, 31, 43, 59]
lista2 = ['Ana', 'José', 'Maria', 'Paulo']
# Podemos criar listas com diversos tipos (float, boolean, etc.) e misturá-los.
# Uma lista que não contém elementos é chamada de lista vazia; podemos criar uma com colchetes vazios.

'''
Podemos usar o comando *len* para saber quantos elementos temos na lista:
'''
print(len(lista1))
print(len(lista2))

'''
Podemos acessar cada elemento da lista por meio de um índice numérico. Em python, o primeiro elemento da lista corresponde ao índice 0:
'''
print(lista1[0])
print(lista1[4])

'''
Para listas de valores inteiros, podemos usar o comando *range* para criar listas:
'''
lista1 = list(range(10)) # lista com números de 0 a 9.
lista2 = list(range(5, 20)) # lista com números de 5 a 19.
lista3 = list(range(10, 0, -1)) # lista regressiva de 10 a 1.
lista4 = list(range(0, 21, 2)) # lista com elementos pares entre 0 e 20.


### REPETIÇÃO E LISTAS ###

'''
Um grande número de computações envolvem o processamento de um item de um conjunto de cada vez. Para listas, isto significa que nós gostaríamos de processar um elemento de cada vez.

Muitas vezes, nós começamos no início, selecionamos o primeiro elemento, fazemos 
alguma coisa com ele, e continuamos até o final. Este padrão de processamento é chamado de *percurso*. 
'''

# Usando for para percorrer listas #
'''
A forma mais comum de percorrer os elementos em uma lista é com um loop for.
'''
frutas = ['pera', 'laranja', 'banana', 'cereja']

for fruta in frutas: # por item
  print(fruta)
# leia como 'para cada item na lista: imprima(item)'
'''
Podemos também usar o índice para acessar os itens iterativamente.
'''
for posicao in range(len(frutas)): # por índice
  print(frutas[posicao])
'''
Neste exemplo, em cada iteração do laço, a variável posição é usada como um índice da lista, imprimindo a posição-ésimo item.

Note que usamos len como limite superior do intervalo de tal forma que podemos iterar corretamente independentemente do número de itens da lista.
'''
# Qualquer expressão sequencial pode ser usada em um laço for. Ex: números inteiros.
for numero in range(21):
  if numero % 3 == 0:
    print(numero, 'é múltiplio de 3.')

### O PADRÃO ACUMULAÇÃO ###

'''
Como somar valores de uma lista? Uma maneira simples é interar sobre a lista, i. e., é manter uma "soma parcial", inicializada com o valor zero, até alcançar o último valor da lista, utilizando uma variável para lembrar da "soma parcial" e atualizando-a.
'''
lista = [10, 25, 31, 43, 59]
soma_parcial = 0

for valor in lista:
  soma_parcial = soma_parcial + valor

print(soma_parcial)

'''
Este padrão de iteração da atualização da variável é chamada comumente como padrão de acumulação. Nos referimos à variável como o acumulador.

A chave para fazer isto funcionar é certificar que a variável é inicializada antes de você começar as iterações.
'''

### O PADRÃO SELEÇÃO ###

'''
Outra atividade comum é percorrer uma lista e selecionar algum elemento (por exemplo, o máximo, o mínimo, etc.). Podemos usar uma ideia parecida com o  padrão acumulação e usar uma variável para indicar qual o elemento atende o critério de seleção até aquele momento, a medidade que percorremos a lista.
'''
# Ex: encontrar o menor elemento.
lista = [10, 25, 31, 43, 59]
menor_parcial = float('inf') # inicializando com 'infinito', pois não sabemos ainda qual seria o menor da lista.
# float('-inf') para infinito negativo.
for valor in lista:
  if valor < menor_parcial:
    menor_parcial = valor

print(menor_parcial)

### O PADRÃO CONTAGEM ###

'''
Um outro caso similar é quando queremos contar a ocorrência de um elemento em uma lista. Podemos criar uma variável auxiliar "contagem parcial", inicialmente com o valor 0. Ao percorrermos a lista, se encontrarmos um elemento igual ao que queremos contar, incrementamos esta contagem parcial em 1:
'''

lista = ['maçã', 'banana', 'maçã', 'melancia', 'limão']

elemento = 'maçã'
contagem_parcial = 0

for fruta in lista:
  if fruta == elemento:
    contagem_parcial = contagem_parcial + 1

print(contagem_parcial)

### LISTAS E FUNÇÕES ###

'''
Assim como as outras variáveis, podemos criar funções que recebem listas como parâmetros. O exemplo a seguir contém uma função que recebe uma lista, e retorna o menor elemento desta lista:
'''
def menor_em_lista(lista):
  menor_parcial = float('inf')
  for valor in lista:
    if valor < menor_parcial:
      menor_parcial = valor
  return(menor_parcial)
  
print(menor_em_lista([50, -1, 8, 40, 7, 21]))

'''
Estamos no final do quadrimestre e a Profa Denise foi responsável pela disciplina de Processamento da Informação (PI). Ela precisa entregar a nota final da disciplina.

A nota final em PI é dada pela razão da soma das notas pelo número de avaliações, sendo que houveram 3 avaliações, valendo de 0 a 10.

A Profa Denise armazenou as notas de cada aluna em listas diferentes. Você como monitora da disciplina decidiu ajudá-la construindo um programa para calcular as notas finais.

Primeiro você precisa retornar a soma das notas e depois a média final. E aí, acha que consegue?
'''
def media(lista):
    total = 0
    for item in lista:
      total = total + item
    return total/len(lista) # todo return retorna uma função

notas1 = [7, 5.8, 9]
notas2 = [10, 6.9, 10]
notas3 = [4.5, 6.2, 7.4]

print('Média notas 1: {:.2f}'.format(media(notas1)))

### Função chamando função

def soma(lista):
    total = 0
    for item in lista:
      total = total + item
    return total

def media(lista):
    return soma(lista)/len(lista)

notas1 = [7, 5.8, 9]
notas2 = [10, 6.9, 10]
notas3 = [4.5, 6.2, 7.4]

print('Média notas 1: {:.2f}'.format(media(notas1)))

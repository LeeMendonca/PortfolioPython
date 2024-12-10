### FUNÇÕES ###

''' Algumas funções já prontas do Python são: '''

# print()   - Imprime na interface
# input()   - Recebe a entrada de dados
# format()  - Formata valores nas linhas de código
# type()    - Retorna o tipo da variável

''' Criando uma função '''

def função(parametro1, parametro2):
  pass # Diz ao intepretador que definiremos os cálculos depois (também pode ser usado nas instruções if, while e for, por exemplo).

def velocidade(espaco, tempo):
  v = espaco/tempo
  print('Velocidade: {} m/s'.format(v))
velocidade(100, 20) # Chama a função.

def diz_oi(): # Função sem parâmetros.
  print('Oieee!!!')
diz_oi()

def dados (nome, idade=None): # Parâmetro opcional.
  print('nome: {}'.format(nome))
  print('idade: {}'.format(idade))
dados('joão')

def velocidade(espaco, tempo):
  v = espaco/tempo
  return v # Retorna o valor calculado. Uma função só pode ter um 'return', mas pode retornar mais de um valor (return a, b).
print(velocidade(100,20))

resultado = velocidade(100, 20) # Atribuindo a função a uma variável.
aceleracao = velocidade(100, 20)/20 # Utilizando a função em outro cálculo. Ou:
aceleracao = resultado/20

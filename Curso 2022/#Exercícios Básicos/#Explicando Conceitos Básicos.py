### CONDICIONAIS ###

''' 
Constantes embutidas no Python: True, False e None.
True e False são valores booleanos que representam, respectivamente, verdadeiro e falso. A função bool() retorna o valor booleano de um argumento.
'''
print(bool(1 == '1'))
'''
A função resulta False em strings vazias, quando um número é 0 ou quando é None. O None é um valor do tipo NoneType e é usado para representar a abstenção de um valor. Em outras linguagens, como Java e C#, é comum utilizar a palavra Null para abstenção de valor.
'''
print(type(None))

''' Operadores '''

# Operadores de Comparação:
'''
a  ==  b : igual
a  !=  b : diferente
a  <   b : menor
a  >   b : maior
a  <=  b : menor ou igual
a  >=  b : maior ou igual
'''
# Operadores com Portas Lógicas:
'''
a   is   b : são idênticos
a is not b : não são idênticos
a   in   b : a é membro de b
a not in b : a não é membro de b
'''
###################################################

''' Comando if e elif '''
# Tentando adivinhar o número:
numero = 21
palpite = int(input('Digite um número: '))
# sem o int o Python fará a comparação (21 == '21'?) e resultará em False.

if palpite == numero: # deve ser um booleano.
  print('Você acertou!')
elif palpite > numero:
  print('Você errou! Seu palpite foi maior que o número secreto.')
else:
  print('Você errou! Seu palpite foi menor que o número secreto.')

##################################################

''' Funções que retornam valores booleanos '''

idade = int(input('Digite a idade: '))

def verificar_maior_idade(idade):
  if idade >= 18:
    return True
  else:
    return False
    
print(verificar_maior_idade(idade))

# ou, de forma mais direta:

def verificar_maior_idade(idade):
  return idade >= 18
print(verificar_maior_idade(idade))
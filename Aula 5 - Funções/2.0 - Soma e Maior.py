# Criando uma função soma.
def soma(a,b):
  print(a+b)

# Criando uma função maior.
def maior(x,y):
  if x > y:
    print(x)
  else:
    print(y)
    
print('Função para soma')
n1 = int(input('n1: '))
n2 = int(input('n2: '))
soma(n1,n2)

print('\nFunção para maior')
n3 = int(input('n3: '))
n4 = int(input('n4: '))
maior(n3,n4)
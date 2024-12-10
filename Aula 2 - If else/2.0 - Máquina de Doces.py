'''
Vamos programar uma máquina de doces!
1. Mostre para o cliente a lista de doces:

FINI → 34 → R$5,00
Chokito → 80 → R$3,00
Sonho de Valsa → 57 → R$1,50
Pão de Mel → 22 → R$6,00

2. Peça para a pessoa inserir o número do doce que ela deseja.
3. Após a pessoa inserir o número, apresente para ela o valor do doce que ela escolheu.

'''

print('Saiba quais doces temos!\n')
print('--------Tabela de Doces---------')
print('| Fini           | 34 | R$5,00 |')
print('| Chokito        | 80 | R$3,00 |')
print('| Sonho de Valsa | 57 | R$1,50 |')
print('| Pão de Mel     | 22 | R$6,00 |')
print('--------------------------------')
# para digitar essa 'barra reta' basta digitar shift + barra invertida.

doce = int(input('\nInsira o número do doce que deseja: '))

if doce == 34:
  print('\nEsse doce custa R$5,00')
elif doce == 80:
  print('\nEsse doce custa R$3,00')
elif doce == 57:
  print('\nEsse doce custa R$1,50')
elif doce == 22:
  print('\nEsse doce custa R$6,00')

while doce != 34 and doce != 80 and doce != 57 and doce != 22:
  # não se esqueça de usar a porta lógica and para que a relação seja verdadeira em todos os casos.
  print('\nDesculpe, não temos um doce com esse número. Tente novamente.')
  doce = int(input('Insira o número do doce que deseja (34, 80, 57 ou 22): '))   
  if doce == 34:
    print('\nEsse doce custa R$5,00')
  elif doce == 80:
    print('\nEsse doce custa R$3,00')
  elif doce == 57:
    print('\nEsse doce custa R$1,50')
  elif doce == 22:
    print('\nEsse doce custa R$6,00')

print('\nFim do programa!')

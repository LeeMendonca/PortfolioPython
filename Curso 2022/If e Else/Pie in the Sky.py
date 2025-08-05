'''
O festival de música Pie in the Sky acontece todo ano.
Você e suas amigas finalmente acreditam que têm idade suficiente para poder ter acesso ao evento.

Para ter acesso liberado ao Pie in the Sky, as visitantes precisam formar um grupo de pelo menos 4 pessoas,
que juntas somam no mínimo 77 anos.

Faça um programa que leia o nome e a idade de cada uma das suas amigas e verifique se vocês conseguirão entrar no evento.

Obs. Não esqueça de imprimir se o grupo poderá ou não participar do Pie in the Sky.
'''
s = 0

grupo = int(input('Quantas meninas estão no grupo? '))

if grupo < 4:
  print('\nQue pena! Vocês não poderão participar do Pie in the Sky :(\nÉ necessário formar um grupo com pelo menos 4 pessoas.')

else:
  for i in range(1, grupo+1):
    nome = input('\nDigite o nome da {}ª visitante: '.format(i))
    idade = int(input('Qual a idade de {} ? '.format(nome)))
    s = s + idade
  
  # print(s)
  
  if s >= 77:
    print('\nParabéns! Vocês poderão participar do Pie in the Sky :)')
  else:
    print('\nQue pena! Vocês não poderão participar do Pie in the Sky :(')

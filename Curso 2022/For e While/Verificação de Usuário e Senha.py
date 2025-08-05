usuario_salvo = 'Leh'
senha_salva = "sereia"

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')
  
for i in range (3):
  if usuario != usuario_salvo or senha != senha_salva:
    print('Usuário ou senha incorretos. Tente novamente: ')
    usuario = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
  elif usuario == usuario_salvo and senha == senha_salva:
    break

if usuario != usuario_salvo or senha != senha_salva:
  print('Limite de tentativas atingido. ')

else:
  print('Bem-vinda, Letícia!')

'''
Escreva um algoritmo no qual a pessoa possa inserir o seu usuário e senha. Faça a verificação da senha com uma senha já salva no código e caso essa senha não seja correta, peça novamente uma outra senha.
'''

senha_salva = "sereias"

usuario = input('Digite seu usuário: ')
senha = input('Digite sua senha: ')

while senha != senha_salva:
  senha = input('A senha está incorreta! Tente novamente: ')
    
print('A senha está correta. Seja bem-vindo(a),', usuario, '!')

# Se a senha estiver correta, não é necessário usar if ou break, pois vai sair automaticamente do loop do while.
'''
Atividade 3

Você e sua vizinha Vanessa foram acampar no gramado da sua casa e decidiram
enterrar um cofre com 50 reais e um bilhete no seu quintal, para as gerações
futuras. No bilhete, vocês escreveram as instruções do quadro:

1) Aqui há um tesouro para quem conseguir desvendar minha senha;
2) Minha senha possui 4 dígitos: são duas letras minúsuculas e dois números;
3) Você tem infinitas tentativas;
4) Aqui vai uma dica para te ajudar: dois patinhos alternados na casa rosa.

Senha: 2c2r

Escreva um programa que funcione de mesma forma que o cofre, tendo como entrada
uma sequência de 4 dígitos e que rode até alcançar a sequência desejada.
'''
print ("=== Cofre no Gramado ===")

while True:
    senha = input("Digite a senha: ")
    
    if senha == "2c2r":
        print("Parabéns, você descobriu a minha senha!")
        break
    else:
        print("Senha incorreta. Tente novamente!")
frase1 = "Olá mundo!"

print(frase1[0:3])
print(frase1[-4:-1])
print(frase1[::-1])
# 1º número: casa de início
# 2º número: casa de término
# 3º: posição (pode-se pular ou imprimir ao contrário)


''' É um palindromo? '''

frase2 = 'sopapos'

def palindromo(frase2):
  if frase2 == frase2[::-1]:
    return True
  else:
    return False

print(palindromo(frase2))


''' Split e Join '''

frase3 = "essa é uma frase com muitas palavras"
lista_palavras=frase3.split()
print(lista_palavras)
###
nova_frase = " ".join(lista_palavras)
print(nova_frase)


''' String e Laços '''

def conta_vogais(texto):
  n_vogais = 0
  for letra in texto:
    if letra in ['a','e','i','o','u']:
      n_vogais = n_vogais + 1
  return n_vogais

frase = input("Digite uma frase: ")
print("O número de vogais é {}.".format(conta_vogais(frase)))
###

def soma_digitos(numero):
  str_numero = str(numero)
  soma = 0
  for digito in str_numero:
    soma = soma + int(digito)
  return soma
    
n = int(input("Digite um número: "))
print("A soma dos dígitos é {}.".format(soma_digitos(n)))


''' Criptografando '''

def criptografa(frase,k):
  criptografada = ""
  for letra in frase:
    criptografada += chr(ord(letra)+k)
  return(criptografada)

frase4 = "Essa frase não está criptografada!" 

criptografada_3 = criptografa(frase4,3) 
print(criptografada_3)

criptografada_5 = criptografa(frase4,5)
print(criptografada_5)

''' Descriptografando '''
def descriptografa(frase,k):
  criptografada = ""
  for letra in frase:
    criptografada += chr(ord(letra)-k)
  return(criptografada)

print(criptografada_3) 
descriptgrafa_3 = descriptografa(criptografada_3,3)
print(descriptgrafa_3)

print(criptografada_5) 
descriptgrafa_5 = descriptografa(criptografada_5,5)
print(descriptgrafa_5)

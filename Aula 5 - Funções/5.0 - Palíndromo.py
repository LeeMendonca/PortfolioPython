frase1 = "Olá mundo!"

print(frase1[0:3])
print(frase1[-4:-1])
print(frase1[::-1])
# 1º número: casa de início
# 2º número: casa de término
# 3º: posição (pode-se pular ou imprimir ao contrário)

''' É um palíndromo? '''

frase2 = 'sopapos'

def palindromo(frase2):
  if frase2 == frase2[::-1]:
    return True
  else:
    return False

print(palindromo(frase2))

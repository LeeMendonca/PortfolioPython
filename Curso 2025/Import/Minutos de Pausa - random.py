'''
Atividade 11

Você quer sortear um número entre 1 e 10 para decidir quantos minutos de pausa
terá no dia. Crie uma função minutos_pausa() que retorna esse número.

Use o import Random e a função dele randint que retorna valores entre um
intervalo de inteiros, por exemplo:

random.randint(1,10) => retorna um número aleatório inteiro entre 1 e 10

'''
print ("=== Minutos de Pausa ===")

import random

def minutos_pausa():
    minutos = random.randint(1, 10)
    print(f"Tempo de intervalo: {minutos} min")

minutos_pausa()

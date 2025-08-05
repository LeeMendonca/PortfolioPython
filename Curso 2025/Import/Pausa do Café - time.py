'''
Atividade 12

Você quer fazer uma pausa de 2 segundos para o café. 
Crie uma função pausa_cafe() que imprime "Pausa iniciada", espera 2 segundos,
e imprime "Pausa finalizada".

Use a função sleep do import time que faz o programa pausar sua execução pela
quantidade de segundos que você determina. Por exemplo:

time.sleep(10) -> o Programa para a execução por 10 segundos e depois
retorna a execução
'''
import time

print ("=== Pausa do Café ===")

def pausa_cafe(tempo):

    print("   Pausa iniciada")
    time.sleep(tempo)
    print("   Pausa finalizada")

s = int(input("Quantos segundos vai durar a pausa? "))
pausa_cafe(s)
'''
Carolina quer acompanhar quantos passos dá por dia para manter uma rotina saudável.
Ela deseja saber se bateu a meta diária de 10.000 passos.

Crie uma função meta_batida(passos) que recebe o número de passos dados em um dia
e retorna "Meta batida!!!" se for igual ou maior que 10.000, ou "Continue se
esforçando!" caso contrário.
'''

def meta_batida(passos):
    
    if passos >= 10000:
        print("Meta batida!!!")
    else: 
        print("Continue se esforçando!")

n = int(input("Digite quantos passos você atingiu hoje: "))
meta_batida(n)

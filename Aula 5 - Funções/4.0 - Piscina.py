'''
Anna tem uma piscina circular com 6m de raio e 1.5m de altura. 
Ela deseja calcular quantos litros de água precisará para enchê-la.
Sabendo que podemos obter o volume de um objeto multiplicando a sua área pela sua altura. 
E que para calcular a área de um círculo multiplicamos a constante π pelo raio ao quadrado.
Crie um programa para ajudá-la.

A = πr²

Dica: Utilize a biblioteca math para obter o valor de π.
'''

import math

def litros(raio, altura):
    area = math.pi * (raio**2)
    volume = area * altura
    # 1m² = 1000L
    litros = volume * 1000
    litros_rounded = round(litros) # arredondando o valor
    return litros_rounded

r = float(input('Digite o raio da piscina em metros: '))
a = float(input('Digite a altura da piscina em metros: '))

print('Para encher a piscina, serão necessários {:.0f} litros.'.format(litros(r,a)))

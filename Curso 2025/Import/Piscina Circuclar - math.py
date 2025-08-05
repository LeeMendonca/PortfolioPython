'''
MODULARIZAÇÃO

Podemos criar partes de um mesmo programa em arquivos diferentes, 
chamados de módulos.

O Python também oferece vários módulos nativos, como o math, com 
diversas funções matemáticas e o sys para acessar funções do sistema.


Atividade 10

Anna tem uma piscina circular com 6m de raio e 1.5m de altura. Ela deseja
calcular quantos litros de água precisará para enchê-la.

A = πr² | Utilize a biblioteca math para obter o valor de π (math.pi)

'''
import math

print("=== Piscina Circular ===")

def piscinaVolumeLitros(raio):
    volume = math.pi * (raio**2) * 1.5 # πr² x h 
    print(f"Volume da piscina circular: {volume:,.2f}m³\n")
    
    litros = volume * 1000 # 1m³ = 1000L
    print(f"Litros necessários: {litros:,.2f}L")

piscinaVolumeLitros(6)
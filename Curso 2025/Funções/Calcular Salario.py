'''
Atividade 5

O fim de ano está chegando e você está a fim de caprichar no look de fim
de ano $$$. Por esta razão, você trabalhou algumas noites em um Buffet e 
decidiu calcular seu salário para planejar as compras.

Faça uma função que calcule seu salário. Você deve inserir o número de
horas trabalhadas, o valor da hora trabalhada e levar em consideração as
condições abaixo:

● Se valor de horas trabalhadas for menor ou igual a 40h, o salário é
a multiplicação da quantidade de horas trabalhadas pelo valor da
hora de trabalho
● Retorne o valor do salário.
Bônus:
● Se o valor de horas for maior que 40h, adicione um valor de hora extra, sendo
o adicional de hora extra de 50%, basta multiplicar a hora por 1,5;

Dica: Lembre-se de converter os valores da quantidade de horas trabalhadas e o
valor da hora trabalhada para tipo float, pois eles serão recebidos como string

por meio da instrução input.

'''
print ("=== Calculando Horas Trabalhadas ===\n")

def calculaSalario (a, b):
    
    if a <= 40:
        return a * b
    else:
        salario = (40*b) + ((a-40)*(b*1.5))
        return salario

qtd_horas = float(input("Digite a quantidade de horas trabalhadas: "))
valor_cada_hora = float(input("Digite o valor de cada hora trabalhada: "))

total = calculaSalario(qtd_horas, valor_cada_hora)
print(f"\nSalário total: R${total:,.2f}")

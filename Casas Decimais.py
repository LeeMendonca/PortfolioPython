# Limitando Casas Decimais - Conversor de Temperatura

C = float(input('Digite o valor de C (temperatura em graus Celsius): '))
# print('Fórmula: C = (F-32)/1.8')
F = float(1.8*C + 32)
print('A temperatura em Fahrenheit é: %.1f °F'%F)

# Outra forma de definir casas decimais:
print('A temperatura em Fahrenheit é: {:.1f} °F'.format(F)) 
# dessa forma, é possível formatar mais variáveis.

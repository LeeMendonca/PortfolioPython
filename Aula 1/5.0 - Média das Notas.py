'''
Atividade 5 - Média das Notas

Uma professora pediu a sua ajuda para calcular as notas de 3 de suas alunas de BCC. A média é calculada pela soma das notas dividido por três. As notas são das provas P1, P2 e P3.

Calcule a média das 3 alunas e apresente no seguinte formato:

Nome : média

'''

print('Digite as notas de cada aluna')

lara_p1 = float(input('Lara P1: '))
lara_p2 = float(input('Lara P2: '))
lara_p3 = float(input('Lara P3: '))

lara_m = ((lara_p1 + lara_p2 + lara_p3) / 3)

erika_p1 = float(input('Erika P1: '))
erika_p2 = float(input('Erika P2: '))
erika_p3 = float(input('Erika P3: '))

erika_m = (erika_p1 + erika_p2 + erika_p3) / 3

thais_p1 = float(input('Thaís P1: '))
thais_p2 = float(input('Thaís P2: '))
thais_p3 = float(input('Thaís P3: '))

thais_m = (thais_p1 + thais_p2 + thais_p3) / 3

print('A média de cada aluna é:')
print('Lara: {:.2f}'.format(lara_m))
print('Erika: {:.2f}'.format(erika_m))
print('Thaís: {:.2f}'.format(thais_m))

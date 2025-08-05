'''
Atividade 14

Ajude a professora Anna a completar o relatório do seu curso
de Python. Ela precisa informar quantas das estudantes irão
receber o certificado ao fim do curso.

Para receber o certificado, a aluna precisa ter presença no
mínimo em 3 das 5 aulas.

Ela informa que a turma possui 10 estudantes com as
seguintes quantidades de faltas, em ordem de chamada:

[0,3,0,0,0,1,2,1,1,0]

Faça um programa que recebe o número de chamada da aluna e
imprime a sua quantidade de faltas

'''
faltas = [0,3,0,0,0,1,2,1,1,0]

aluna = int(input("Digite o número da aluna: "))

print("Quantidade de faltas: ", faltas[aluna-1])

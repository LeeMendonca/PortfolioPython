'''
Atividade 9

Vamos ajudar a Profa Denise com o cálculo das notas finais da disciplina de PI?

Ela precisa de ajuda para converter as notas para os conceitos da UFABC de 
acordo com a tabela:

CONCEITO NOTA (n)
A: n>= 9.0
B: 7.5 <= n < 9.0
C: 6.5 <= n < 7.5
D: 5.0 <= n < 6.5
F: n < 5

Como você construiria esse programa utilizando uma função em Python?
'''
print ("=== Convertendo Notas em Conceitos ===\n")

def converte_nota_em_conceito(n):
    
    if n >= 9.0:
        return "A"
    elif n >= 7.5:
        return "B"
    elif n >= 6.5:
        return "C"
    elif n >= 5.0:
        return "D"
    else:
        return "F"

nota = float(input("Digite a nota do aluno(a): "))
conceito = converte_nota_em_conceito(nota)

print(f"{nota:,.2f} → {conceito}")
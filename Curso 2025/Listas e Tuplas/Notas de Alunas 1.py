'''
Atividade 15

Após Anna escrever a lista com as notas das alunas, ela
percebeu que cometeu dois erros na conferência da lista
de presença. A terceira aluna da lista teve na verdade
duas faltas ao invés de zero e a oitava aluna teve três
faltas ao invés de uma.

Escreva um código simulando essa alteração na lista,
utilizando a alteração de itens por índice.
faltas_iniciais = [0,3,0,0,0,1,2,1,1,0]

'''

faltas = [0,3,0,0,0,1,2,1,1,0]

faltas[2] = 2
faltas[7] = 3

print(f"Faltas corrigidas: {faltas}")

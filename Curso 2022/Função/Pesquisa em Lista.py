'''
Função é igual a método (pesquisar no material)
'''
def pesquise(lista, valor):
    index = 0
    for item in lista: # for item not in lista, return None
      if item == valor:
        return index

L = [10, 20, 25, 30]
print(pesquise(L, 25))
print(pesquise(L, 27))
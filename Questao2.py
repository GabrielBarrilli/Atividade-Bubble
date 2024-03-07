import random

# Função para encontrar o k-ésimo menor elemento da lista
def k_esimo(lista, k):
    lista_ordenada = sorted(lista)
    k_esimo_elemento = lista_ordenada[k-1]
    return k_esimo_elemento

# Função para contar o número mínimo e máximo de comparações
def contar_comparacoes(lista):
    n = len(lista)
    comparacoes_minimas = n - 1
    comparacoes_maximas = (n*(n-1)) // 2
    return comparacoes_minimas, comparacoes_maximas

# Cria uma lista com números aleatórios
lista = random.sample(range(1, 101), 10)
print("Lista original:", lista)

# Encontra o k-ésimo menor elemento (k=1 neste caso)
k = 1
k_esimo_elemento = k_esimo(lista, k)
print(f"{k}-ésimo menor elemento da lista: {k_esimo_elemento}")

# Conta o número mínimo e máximo de comparações
comparacoes_minimas, comparacoes_maximas = contar_comparacoes(lista)
print("Número mínimo de comparações:", comparacoes_minimas)
print("Número máximo de comparações:", comparacoes_maximas)

# teste
import random

# Função para verificar se a lista está ordenada
def esta_ordenada(lista):
    return all(lista[i] <= lista[i + 1] for i in range(len(lista) - 1))

# Cria uma lista com 10 números aleatórios
lista = random.sample(range(1, 101), 10);
print("Lista original:", lista)

# Bubble Sort
comparacoes_minimas = 0
comparacoes_maximas = 0
ordenado = False

while not ordenado:
    ordenado = True
    for i in range(len(lista) - 1):
        comparacoes_maximas += 1
        if lista[i] > lista[i + 1]:
            lista[i], lista[i + 1] = lista[i + 1], lista[i]
            ordenado = False
    comparacoes_minimas += 1

print("Lista ordenada:", lista)
print("Número mínimo de comparações:", comparacoes_minimas)
print("Número máximo de comparações:", comparacoes_maximas)

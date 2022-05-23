"""
Programação Estruturada
2022.1
23/05/2022

- Mais sobre listas
    - Pilhas/Filas
    - Matrizes
- Dicionários
"""

def pilha_insere(lista, valor):
    lista.append(valor)

def pilha_remove(lista):
    return lista.pop()

def pilha_testa():
    pilha = []
    pilha_insere(pilha, 4)
    pilha_insere(pilha, 7)
    pilha_insere(pilha, 9)
    print(pilha)
    for _ in range(2):
        pilha_remove(pilha)

    print(pilha)

pilha_testa()

def fila_remove(lista):
    if lista:
        return lista.pop(0)

matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sudoku = [
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
]

print(sudoku[6][4])

# Dicionários

alunos = ["a", "b", "c", "d", "e"]
notas = [4.0, 5.5, 9.2, 8.7, 6.6]

for indice, aluno in enumerate(alunos):
    print(aluno, notas[indice])

pauta = {
    # chave: valor
    "a": 4.0,
    "b": 5.5,
    "c": 9.2,
    "d": 8.7,
    "e": 6.6
}

print(f"{pauta['c']:.2f}")
print(pauta)

pauta["f"] = 7.8
print(pauta)
print(pauta.keys())
print(pauta.values())

if "h" in pauta:
    print(pauta["h"])

# iterar pelas chaves
for aluno in pauta:
    print(aluno)

# iterar pelos valores
for nota in pauta.values():
    print(nota)

# iterar pelo dicionário inteiro
for aluno, nota in pauta.items():
    print(aluno, nota)

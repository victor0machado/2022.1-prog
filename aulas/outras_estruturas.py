"""
Programação Estruturada
2022.1

18/05/22
Mais algumas estruturas de dados

Tuplas
Conjuntos
"""

# Tuplas
# Estruturas imutáveis
alunos = ["aaa", "bbb", "ccc"]
notas = [6.5, 7.8, 4.2]

def procura_nota(
        nome_procurado,
        nomes,
        numeros
    ):
    """
    Retorna um par (nome, nota) para um
    dado nome em nomes
    """
    for indice, nome in enumerate(nomes):
        if nome == nome_procurado:
            return (nome, numeros[indice])

    print(f"{nome_procurado} não encontrado!")
    return ("Não encontrado!", -1.0)

aluno = procura_nota(
    "bbb",
    alunos,
    notas
) # 7.8

print(aluno[0])
print(aluno[1])

alunos = {"a", "b", "c", "d", "a"}
print(alunos)

alunos = ["a", "b", "c", "d", "a"]
print(alunos)
alunos = set(alunos)

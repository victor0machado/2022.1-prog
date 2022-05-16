"""
2022.1 - Programação Estruturada
16/05/2022

Listas
"""

lista = [10, 1.45, "texto", True, False, [], {}]

alunos = ["abc", "def", "ghi"]
print(alunos[1])
print(alunos[-1])

# fatiamento
# slicing
# range(start, stop, step)
alunos = [
    "abc", "def", "ghi", "jkl",
    "mno", "pqr", "stu", "vwx"
]

premiados = alunos[0:3] # "abc", "def", "ghi"
premiados = alunos[:3] # "abc", "def", "ghi"
pares = alunos[1::2]
lista = alunos[::3]
ordem_inversa = alunos[::-1]

print(ordem_inversa)

alunos.append("yza")
print(alunos)

alunos.insert(4, "aaa")
print(alunos)

alunos.extend(["bbb", "ccc", "ddd"])
print(alunos)

alunos.pop()
print(alunos)

alunos.pop(4)
print(alunos)

aluno = alunos.pop()
print(aluno)
print(f"{aluno} foi eliminado!")

alunos.remove("ghi")
print(alunos)

# Vai subir uma exceção!
# alunos.remove("xpto")

indice = alunos.index("def")
print(indice)

# Vai subir uma exceção!
# indice = alunos.index("xpto")

if "xpto" in alunos:
    alunos.remove("xpto")

for aluno in alunos:
    print(aluno)

# Evitar usar essa estrutura!
for indice in range(len(alunos)):
    print(alunos[indice])

for indice, aluno in enumerate(alunos):
    print(indice, aluno, sep=" - ")

for indice, _ in enumerate(alunos):
    print(indice)

alunos = [
    "abc", "def", "ghi", "ghi",
    "jkl", "ghi", "mno", "pqr",
    "ghi", "stu", "ghi", "vwx"
]

# eliminar todos os elementos "ghi"
# da lista alunos
# while "ghi" in alunos:
#     alunos.remove("ghi")

# listas são passadas por referência
def remove_elem_inplace(elem, lista_a_remover):
    """
    Remove todas as referências de elem
    in lista.
    """
    while elem in lista_a_remover:
        lista_a_remover.remove(elem)

remove_elem_inplace("ghi", alunos)
print(alunos)

alunos = [
    "abc", "def", "ghi", "ghi",
    "jkl", "ghi", "mno", "pqr",
    "ghi", "stu", "ghi", "vwx"
]

def remove_elem(elem, lista_a_remover):
    """
    Remove todas as referências de elem
    in lista, e retorna para uma nova
    lista.
    """
    lista_limpa = []

    for item in lista_a_remover:
        if item != elem:
            lista_limpa.append(item)

    return lista_limpa

lista2 = remove_elem("ghi", alunos)
print(lista2)
print(alunos)

"""
Manipula informações sobre um aluno.
"""

def cria_aluno(nome, matricula):
    """Cria um dicionário com dados de um aluno."""
    return {
        "nome": nome,
        "matricula": matricula
    }

def adiciona_nota(aluno, nota):
    """Adiciona uma nota ao aluno."""
    if "notas" in aluno:
        aluno["notas"].append(nota)
    else:
        aluno["notas"] = [nota]

def info_aluno(aluno):
    """Exibe na tela informações sobre alunos."""
    print(aluno["nome"], aluno["matricula"], sep=" - ")
    if "notas" in aluno:
        for nota in aluno["notas"]:
            print(nota)

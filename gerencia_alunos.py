from src import aluno

def main():
    alunos = []

    alunos.append(aluno.cria_aluno("abc", 123))
    alunos.append(aluno.cria_aluno("def", 456))
    alunos.append(aluno.cria_aluno("ghi", 789))

    aluno.adiciona_nota(alunos[0], 8.5)
    aluno.adiciona_nota(alunos[0], 7.6)

    for alu in alunos:
        aluno.info_aluno(alu)

main()

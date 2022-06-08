"""
Detalha a classe Aluno.
"""

class Aluno:
    """Informações sobre um aluno da faculdade."""
    def __init__(self, matricula, nome, cpf):
        self.matricula = matricula
        self.nome = nome
        self.cpf = cpf
        self.curso = ""
        self.disciplinas = []

    def inscrever_curso(self, curso):
        """Inscreve o aluno em um curso."""
        self.curso = curso

    def adicionar_disciplina(self, disciplina):
        """Adiciona uma disciplina às disciplinas do curso."""
        self.disciplinas.append(disciplina)

    def __repr__(self):
        msg = f"{self.matricula} - {self.cpf} - {self.nome}"
        msg += f"\n{self.curso}\n"
        msg += "\n".join(self.disciplinas)
        return msg

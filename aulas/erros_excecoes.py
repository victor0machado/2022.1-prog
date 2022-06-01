"""
Programação Estruturada
2022.1
25/05/2022
Tratamento de Erros e Exceções
"""

lista = [1, 2, 3]
lista.remove(3)

alunos = {
    "a": 123,
    "b": 456
}

if "c" in alunos:
    print(alunos["c"])

class InvalidCpfError(Exception):
    pass

def valida_cpf(valor):
    if valor % 2:
        raise InvalidCpfError("O valor do CPF é inválido!")

# try / except
while True:
    try:
        cpf = int(input("Informe o CPF: "))
    except ValueError:
        print("Informe apenas números.")
    else: # roda apenas se não entrar em nenhum except.
        valida_cpf(cpf)
        break

arq = None

try:
    arq = open("teste.py")
except FileNotFoundError:
    arq = open("readme.md", "a")
except FileExistsError:
    print("O arquivo já existe!")
finally: # executa independente de ter entrado no except.
    # escrever(arq, "bom dia!")
    if arq:
        arq.close()
    print("-" * 40)

total_notas = 5
divisor = float(input("Informe um número: "))

try:
    print(total_notas / divisor)
except ZeroDivisionError:
    print("ERRO FATAL - mensagem de erro explicando pq fechou.")
    exit()

def func1(num):
    print(5 / num)

def func2():
    func1(0)

def func3():
    func2()

func3()

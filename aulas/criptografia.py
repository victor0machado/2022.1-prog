"""
Programação Estruturada
2022.1
23/05/2022
Aplicação de listas e dicionários
"""
from cripto import cripto

def main():
    """Ponto de entrada do programa."""
    chave = cripto.gera_chave()
    opcoes = {
        "1": cripto.cripto,
        "2": cripto.decripto
    }

    while True:
        msg = input("Informe uma mensagem: ")
        if msg == "":
            break
        oper = input("Informe uma opção: ")
        if oper not in opcoes:
            break

        print(opcoes[oper](msg, chave))

if __name__ == "__main__":
    main()

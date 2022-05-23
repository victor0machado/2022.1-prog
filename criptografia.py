"""
Programação Estruturada
2022.1
23/05/2022
Aplicação de listas e dicionários
"""
import random

def alfabeto():
    """Retorna um alfabeto minúsculo."""
    return [chr(i) for i in range(97, 123)]

def gera_chave():
    """Retorna uma chave criptográfica gerada aleatoriamente."""
    alfa = alfabeto() # De "a" a "z", em ordem
    alfa_random = alfabeto()
    random.shuffle(alfa_random) # alfabeto embaralhado

    chave = {}
    for indice, letra in enumerate(alfa):
        chave[letra] = alfa_random[indice]

    # return {chave[letra]: alfa_random[indice] for indice, letra in enumerate(alfa)}
    return chave

def cripto(mensagem, chave):
    """Retorna uma mensagem criptografada."""
    msg_cripto = ""

    for letra in mensagem:
        msg_cripto += chave[letra]

    return msg_cripto

def decripto(mensagem, chave):
    """Retorna uma mensagem decriptografada."""
    chave_decripto = {}
    for letra, letra_cripto in chave.items():
        chave_decripto[letra_cripto] = letra

    return cripto(mensagem, chave_decripto)

def main():
    """Ponto de entrada do programa."""
    chave = gera_chave()
    opcoes = {
        "1": cripto,
        "2": decripto
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

"""
Implementa falas do ator 2.
"""
from jogo.sons import vozes

def falar():
    """Fala do ator 2."""
    print("Oi! Eu sou o ator 2.")
    vozes.emitir_som(False)

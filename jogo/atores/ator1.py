"""
Implementa falas do ator 1.
"""
from . import ator2
from ..sons import vozes

def falar():
    """Fala do ator 1."""
    print("Oi! Eu sou o ator 1.")
    vozes.emitir_som()

def conversar():
    """Conversa entre os dois atores."""
    falar()
    ator2.falar()

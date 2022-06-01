"""
Emite informações sobre as vozes.
"""

def emitir_som(voz_aguda=True):
    """Emite um som de voz."""
    if voz_aguda:
        print("Você ouviu num tom bem agudo.")
    else:
        print("Você ouviu uma voz grave.")

"""
Programação Estruturada
2022.1
30/05/2022

Módulos
"""
# imports da biblioteca padrão
import sys
import math
import time
import math as mt

from math import fabs, ceil
from math import factorial as fact

# NUNCA USAR!!!!!
from math import *

# imports de bibliotecas externas

# imports de módulos locais

print(math.factorial(8))
print(math.floor(5.55))
print(mt.log(8, 2))

print(math.fabs(-5))
print(fabs(-5))

print(prod([2, 4, 8]))


TEMPO_MAXIMO = 30

def main():
    num = 1
    inicio = time.time()
    while time.time() - inicio < TEMPO_MAXIMO:
        print(num)
        num += 1


if __name__ == "__main__":
    sys.exit(main())

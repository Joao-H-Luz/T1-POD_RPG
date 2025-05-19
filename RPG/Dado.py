# Bibliotecas Utilizadas
from random import *
from abc import ABC, abstractmethod

# -- Dado --

class Dado(ABC):
    def __init__(self, lados: int):
        super().__init__()
        self.lados = lados  # Quantos Lados tem o Dado

    @abstractmethod
    def jogar(self):        # Metodo que Simula jogar o Dado
        pass

    @abstractmethod
    def __repr__(self):     # Metodo de Representação da Classe
        pass

#  -===============================================-  #

    # Metodos de Comparação de Dados

    def __eq__(self, dado):                 # Metodo de Comparação ==
        return self.lados == dado.lados

    def __ne__(self, dado):                 # Metodo de Comparação !=
        return self.lados != dado.lados

    def __lt__(self, dado):                 # Metodo de Comparação <
        return self.lados < dado.lados

    def __le__(self, dado):                 # Metodo de Comparação <=
        return self.lados <= dado.lados

    def __gt__(self, dado):                 # Metodo de Comparação >
        return self.lados > dado.lados

    def __ge__(self, dado):                 # Metodo de Comparação >=
        return self.lados >= dado.lados

#  -================================================================================================================================================-  #

# SubClass || Dado

# -- DADO de 4 Lados --

class D4(Dado):
    def __init__(self):
        super().__init__(lados=4)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado

    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 6 Lados --

class D6(Dado):
    def __init__(self):
        super().__init__(lados=6)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado

    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 8 Lados --

class D8(Dado):
    def __init__(self):
        super().__init__(lados=8)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado

    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 10 Lados --

class D10(Dado):
    def __init__(self):
        super().__init__(lados=10)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado

    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 12 Lados --

class D12(Dado):
    def __init__(self):
        super().__init__(lados=12)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado

    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 20 Lados --
# Dado Padrão de Ataque

class D20(Dado):
    def __init__(self):
        super().__init__(lados=20)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado

    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -===============================================-  #

# -- DADO de 2 Lados (Habilidade) --

class D2(Dado):
    def __init__(self):
        super().__init__(lados=2)

    def jogar(self):                # Metodo que Simula jogar o Dado
        numero_do_dado = randint(1, self.lados)
        return numero_do_dado
    
    def __repr__(self):             # Metodo de Representação da Classe
        return (f"{self.lados} Lados")

#  -================================================================================================================================================-  #
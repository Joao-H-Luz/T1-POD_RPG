# Bibliotecas Utilizadas
from abc import ABC, abstractmethod
from .Dado import *


#  -================================================================================================================================================-  #

# -- Classe --

class Classe(ABC):
    def __init__(self, classe: str, pontos_vida: float, dado_de_ataque: int,
                 pontos_ataque: float, pontos_defesa: float, limite_habilidades: int):
        super().__init__()
        self.classe = classe  # Nome da Classe
        self.pontos_vida = pontos_vida  # Vida do Objeto
        self.dado_de_ataque = dado_de_ataque
        # Dado de Ataque mais Pontos de Ataque == Ataque Final
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        # Limite de Habilidades que a Classe pode ter no Inventario
        self.limite_habilidades = limite_habilidades

    @abstractmethod
    def __repr__(self):
        pass

    def __str__(self):
        return (f"Classe: {self.classe} | Vida: {self.pontos_vida} | Dado de Ataque: {self.dado_de_ataque} | "
                f"Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Limite de Habilidades: {self.limite_habilidades}")

    def __repr__(self):
        return super().__repr__()
    
#  -================================================================================================================================================-  #

# SubClass || Classe

class Guerreiro(Classe):
    def __init__(self):
        super().__init__(classe="Guerreiro",
                         pontos_vida=50,
                         dado_de_ataque=D12(),
                         pontos_ataque=6,
                         pontos_defesa=8,
                         limite_habilidades=2)

    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")

#  -================================================================================================================================================-  #

class Mago(Classe):
    def __init__(self):
        super().__init__(classe="Mago",
                         pontos_vida=14,
                         dado_de_ataque=D6(),
                         pontos_ataque=10,
                         pontos_defesa=3,
                         limite_habilidades=5)

    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")

#  -================================================================================================================================================-  #

class Ladino(Classe):
    def __init__(self):
        super().__init__(classe="Ladino",
                         pontos_vida=21,
                         dado_de_ataque=D8(),
                         pontos_ataque=8,
                         pontos_defesa=5,
                         limite_habilidades=3)

    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")

#  -================================================================================================================================================-  #

class Bardo(Classe):
    def __init__(self):
        super().__init__(classe="Bardo",
                         pontos_vida=15,
                         dado_de_ataque=D10(),
                         pontos_ataque=5,
                         pontos_defesa=5,
                         limite_habilidades=5)

    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")

#  -================================================================================================================================================-  #

class Barbaro(Classe):
    def __init__(self):
        super().__init__(classe="Barbaro",
                         pontos_vida=15,
                         dado_de_ataque=D6(),
                         pontos_ataque=5,
                         pontos_defesa=5,
                         limite_habilidades=0)

    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")

#  -================================================================================================================================================-  #

class Lorde_Abissal(Classe):
    def __init__(self):
        super().__init__(classe="Lorde Abissal",
                         pontos_vida=100,
                         dado_de_ataque=D20(),
                         pontos_ataque=10,
                         pontos_defesa=10,
                         limite_habilidades=0)

    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")
    
#  -================================================================================================================================================-  #


class Smaug_Dourado(Classe):
    def __init__(self):
        super().__init__(classe="🐉 Smaug, o Dourado",
                         pontos_vida=200,
                         dado_de_ataque=D20(),
                         pontos_ataque=10,
                         pontos_defesa=12,
                         limite_habilidades=0)

    def __repr__(self):
        return (f"Classe: {self.classe} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")
#  -================================================================================================================================================-  #
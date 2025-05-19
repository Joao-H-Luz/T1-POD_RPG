# Bibliotecas Utilizadas
from abc import ABC, abstractmethod
from .Dado import *

# -- Habilidade --

class Habilidade(ABC):
    def __init__(self, nome: str, descricao: str, pontos_ataque: int):
        self.nome = nome
        self.descricao = descricao
        self.pontos_ataque = pontos_ataque

    @abstractmethod
    def usar(self):  # Metodo que simula uzar a Habilidade
        pass

    @abstractmethod
    def __str__(self):
        pass

#  -================================================================================================================================================-  #

# SubClass || Habilidade

class BolaDeFogo(Habilidade):
    def __init__(self):
        super().__init__(nome="Bola de Fogo",
                         descricao="Uma bola de fogo que causa dano em área.",
                         pontos_ataque=10)

    def usar(self, alvo):       # Fazer um Metodo que simula uzar a Habilidade
        try:
            alvo.pontos_vida -= self.pontos_ataque
            return self.pontos_ataque
        except AttributeError as e:
            print(f"[Erro] ao usar {self.nome}: alvo inválido - {e}")
            return 0

    def __str__(self):
        return (f"{self.nome}")

    def __repr__(self):
        return (f"{self.nome} | {self.descricao} | Causa {self.pontos_ataque} de Dano")

#  -===============================================-  #

class Cura(Habilidade):
    def __init__(self):
        super().__init__(nome="Cura",
                         descricao="Uma cura que recupera vida.",
                         pontos_ataque=10)

    def usar(self, alvo):       # Fazer um Metodo que simula uzar a Habilidade
        alvo.pontos_vida += self.pontos_ataque  # Cura O personagem
        return self.pontos_ataque

    def __str__(self):
        return (f"{self.nome}")

    def __repr__(self):
        return (f"{self.nome} | {self.descricao} | Recupera {self.pontos_ataque} de Vida")

#  -===============================================-  #

class TiroDeArco(Habilidade):
    def __init__(self):
        super().__init__(nome="Disparo com Arco",
                         descricao="Um tiro de precisão com Arco!",
                         pontos_ataque=6)

    def usar(self, alvo):       # Fazer um Metodo que simula uzar a Habilidade
        alvo.pontos_vida -= self.pontos_ataque
        return self.pontos_ataque

    def __str__(self):
        return (f"{self.nome}")

    def __repr__(self):
        return (f"{self.nome} | {self.descricao} | Causa {self.pontos_ataque} de Dano")

#  -================================================================================================================================================-  #

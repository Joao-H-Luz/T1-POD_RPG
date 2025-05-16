# Bibliotecas Utilizadas
from abc import ABC, abstractmethod
from random import randint

# Classes Obrigatórias:

class Dado(ABC):
    def __init__(self, lados:int):
        super().__init__()
        self.lados = lados

    @abstractmethod
    def jogar(self):
        numero_do_dado = randint(1, self.lados + 1)
        return numero_do_dado
    
class Classe(ABC):
    def __init__(self, nome:str, pontos_vida:float, dado_de_ataque:int,
                 pontos_ataque:float, pontos_defesa:float, limite_habilidades:int):
        super().__init__()
        self.nome = nome
        self.pontos_vida = pontos_vida
        self.dado_de_ataque = dado_de_ataque
        self.pontos_ataque = pontos_ataque
        self.pontos_defesa = pontos_defesa
        self.limite_habilidades = limite_habilidades

    @abstractmethod
    def __str__(self):
        return (f"Nome: {self.nome} | Ataque: {self.pontos_ataque} | Defesa: {self.pontos_defesa} | Tipo de Dado: {self.dado_de_ataque}")

class Habilidade:
    def __init__(self, nome:str, descricao:str, pontos_ataque:str):
        self.nome = nome
        self.descricao = descricao
        self. pontos_ataque = pontos_ataque

    @abstractmethod
    def usar(self):
        pass

class Personagem:
    instancias = 0

    def __init__(self, nome_personagem: str, Classe: Classe, inventario: list):
        self.nome_personagem = nome_personagem
        self.pontos_vida = Classe.self.pontos_vida
        self.dado_de_ataque = Classe.self.dado_de_ataque
        self.pontos_ataque = Classe.self.pontos_ataque
        self.pontos_defes = Classe.self.pontos_defes
        self.limite_habilidade = Classe.self.limite_habilidade
        self.inventario = inventario
        Personagem.instancias += 1

    @classmethod
    def qntd_instancias(cls):
        return cls.instancias

    def atacar(self, alvo):
        pass

    def usar_habilidade(self, alvo):
        pass

